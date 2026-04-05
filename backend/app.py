from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Evolut API running"

# Ruta para registrar usuario
@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    nombre = data.get("nombre")
    email = data.get("email")
    password = data.get("password")

    return jsonify({
        "message": "Usuario recibido",
        "data": {
            "nombre": nombre,
            "email": email
        }
    })

if __name__ == "__main__":
    app.run(debug=True)