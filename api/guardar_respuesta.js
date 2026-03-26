export default async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", ["POST"]);
    return res.status(405).json({ error: "Method not allowed" });
  }

  const body = req.body || {};
  if (!body.answers || typeof body.answers !== "object") {
    return res.status(400).json({ error: "Faltan datos" });
  }

  // Nota: esta funciÃ³n no persiste datos. Para demo, solo valida y responde OK.
  // Si quieres persistencia, conecta una BD externa (Vercel KV, Postgres, etc.).
  return res.status(200).json({ mensaje: "Respuestas recibidas" });
}
