from flask import Flask, request, jsonify
import json
import yaml

app = Flask(__name__)

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_PASSWORD = config.get("api_password", "changeme")

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "pong"}), 200

@app.route("/memoire", methods=["POST"])
def enregistrer_memoire():
    if request.headers.get("Authorization") != API_PASSWORD:
        return jsonify({"error": "Unauthorized"}), 403
    donnees = request.get_json()
    try:
        with open("elios_memoire.json", "w", encoding="utf-8") as f:
            json.dump(donnees, f, ensure_ascii=False, indent=2)
        return jsonify({"message": "Mémoire enregistrée."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/memoire", methods=["GET"])
def lire_memoire():
    if request.headers.get("Authorization") != API_PASSWORD:
        return jsonify({"error": "Unauthorized"}), 403
    try:
        with open("elios_memoire.json", "r", encoding="utf-8") as f:
            contenu = json.load(f)
        return jsonify(contenu), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.get("port", 5000))
