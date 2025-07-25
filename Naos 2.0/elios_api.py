from flask import Flask, request, jsonify
from elios_agent import EliosAgent
import json

app = Flask(__name__)

# Chargement de config
with open("config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

elios = EliosAgent(config)

@app.route("/memoire", methods=["POST"])
def memoriser():
    data = request.json
    cle = data.get("cle")
    contenu = data.get("message")

    if not cle or not contenu:
        return jsonify({"status": "error", "message": "Clé ou message manquant"}), 400

    elios.memoriser(cle, contenu)
    return jsonify({"status": "ok", "message": f"Souvenir '{cle}' enregistré."}), 200


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok", "message": "Naos est en ligne."}), 200


if __name__ == "__main__":
    app.run(port=5000)
