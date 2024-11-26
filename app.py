from flask import Flask, jsonify
from flask_cors import CORS
import speedtest
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/speedtest": {"origins": ["https://www.speeds-test.com"]}})

@app.route('/', methods=['GET'])
def home():
    return "Bienvenido a la aplicación Speedtest"

@app.route('/speedtest', methods=['GET'])
def run_speedtest():
    # Inicializa el cliente de Speedtest
    st = speedtest.Speedtest()

    # Especifica el ID del servidor de prueba que deseas usar
    # server_id = ["40458"]  # Reemplaza 12345 con el ID del servidor deseado
    # st.get_servers(server_id)
    st.get_best_server()  # Selecciona el servidor especificado

    # Realiza la prueba de velocidad
    download_speed = st.download() / 1_000_000 # Convierte a Mbps
    upload_speed = st.upload() / 1_000_000    # Convierte a Mbps
    ping = st.results.ping                     # Latencia en ms

    # Retorna los resultados en formato JSON
    return jsonify({
        "download_speed_mbps": round(download_speed, 2),
        "upload_speed_mbps": round(upload_speed, 2),
        "ping_ms": round(ping, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)