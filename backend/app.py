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

if __name__ == "__main__":
    app.run(debug=True)