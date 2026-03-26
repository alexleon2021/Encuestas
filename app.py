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
    nombre = request.form.get("nombre")
    respuesta = request.form.get("respuesta")

    if not nombre or not respuesta:
        return jsonify({"error": "Faltan datos"}), 400

    insertar_respuesta(nombre, respuesta)
    return jsonify({"mensaje": "Respuesta guardada correctamente"})

# Ruta para ver todas las respuestas (opcional)
@app.route("/respuestas")
def ver_respuestas():
    respuestas = obtener_respuestas()
    return jsonify(respuestas)

if __name__ == "__main__":
    crear_tabla()  # Asegurarse de que la tabla exista
    app.run(debug=True)