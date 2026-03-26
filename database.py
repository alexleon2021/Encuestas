import sqlite3

def conectar_db():
    # Conexión a la base de datos SQLite
    conexion = sqlite3.connect("encuestas.db")
    return conexion

def crear_tabla():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Crear tabla ejemplo
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            respuesta TEXT NOT NULL
        )
    ''')

    conexion.commit()
    conexion.close()

def insertar_respuesta(nombre, respuesta):
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Insertar datos en la tabla
    cursor.execute('''
        INSERT INTO respuestas (nombre, respuesta)
        VALUES (?, ?)
    ''', (nombre, respuesta))

    conexion.commit()
    conexion.close()

def obtener_respuestas():
    conexion = conectar_db()
    cursor = conexion.cursor()

    # Consultar datos de la tabla
    cursor.execute('SELECT * FROM respuestas')
    resultados = cursor.fetchall()

    conexion.close()
    return resultados

if __name__ == "__main__":
    # Crear tabla al ejecutar el script
    crear_tabla()
    print("Base de datos y tabla creadas correctamente.")