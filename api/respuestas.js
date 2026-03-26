import pkg from "pg";

const { Pool } = pkg;

let pool;
let initialized = false;

function getPool() {
  if (!pool) {
    const connectionString =
      process.env.POSTGRES_URL ||
      process.env.POSTGRES_URL_NON_POOLING ||
      process.env.DATABASE_URL;

    if (!connectionString) {
      throw new Error("Falta POSTGRES_URL o DATABASE_URL en variables de entorno");
    }

    pool = new Pool({
      connectionString,
      ssl: process.env.NODE_ENV === "production" ? { rejectUnauthorized: false } : false,
    });
  }
  return pool;
}

async function ensureTable() {
  if (initialized) return;
  const sql = `
    CREATE TABLE IF NOT EXISTS survey_responses (
      id SERIAL PRIMARY KEY,
      created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
      answers JSONB NOT NULL
    );
  `;
  await getPool().query(sql);
  initialized = true;
}

export default async function handler(req, res) {
  try {
    await ensureTable();

    if (req.method === "GET") {
      const result = await getPool().query(
        "SELECT id, created_at, answers FROM survey_responses ORDER BY id ASC"
      );
      return res.status(200).json(result.rows);
    }

    if (req.method === "DELETE") {
      await getPool().query("TRUNCATE TABLE survey_responses");
      return res.status(200).json({ mensaje: "Datos borrados" });
    }

    res.setHeader("Allow", ["GET", "DELETE"]);
    return res.status(405).json({ error: "Method not allowed" });
  } catch (err) {
    return res.status(500).json({ error: err.message || "Error interno" });
  }
}
