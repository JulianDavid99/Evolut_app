from flask import Flask, request, jsonify
from db import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    return "Evolut API running"

@app.route('/test-db')
def test_db():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1;")
        result = cursor.fetchone()
        conn.close()
        return {"message": "Conexion exitosa", "resultado": result}
    except Exception as e:
        return {"error": str(e)}

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()

        nombre = data.get("nombre")
        email = data.get("email")
        password = data.get("password")

        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO usuarios (nombre, correo, contrasena)
        VALUES (%s, %s, %s)
        RETURNING id;
        """

        cursor.execute(query, (nombre, email, password))
        user_id = cursor.fetchone()[0]

        conn.commit()
        conn.close()

        return {
            "message": "Usuario guardado",
            "user_id": user_id
        }

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(debug=True)