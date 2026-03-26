from flask import Flask, request, jsonify, render_template
from database import crear_tabla, insertar_respuesta, obtener_respuestas

app = Flask(__name__)

# Ruta para mostrar el formulario
@app.route("/")
def formulario():
    return render_template("encuesta_TIC.html")

# Ruta para manejar las respuestas del formulario
@app.route("/guardar_respuesta", methods=["POST"])
def guardar_respuesta():
    data = request.get_json()  # Obtener datos en formato JSON
    if not data or "answers" not in data:
        return jsonify({"error": "Faltan datos"}), 400

    # Guardar cada respuesta en la base de datos
    for pregunta, respuesta in data["answers"].items():
        insertar_respuesta(pregunta, respuesta)

    return jsonify({"mensaje": "Respuestas guardadas correctamente"})

# Ruta para ver todas las respuestas (opcional)
@app.route("/respuestas")
def ver_respuestas():
    respuestas = obtener_respuestas()
    return jsonify(respuestas)

if __name__ == "__main__":
    crear_tabla()  # Asegurarse de que la tabla exista
    app.run(debug=True)