import json
import os

MEMOIRE_PATH = "elios_memoire.json"

def charger_memoire():
    if not os.path.exists(MEMOIRE_PATH):
        return []

    with open(MEMOIRE_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            if not isinstance(data, list):
                return []  # sécurité en cas de {}
            return data
        except json.JSONDecodeError:
            return []


def enregistrer_memoire(message, reponse):
    memoire = charger_memoire()
    memoire.append({"message": message, "reponse": reponse})
    with open(MEMOIRE_PATH, "w", encoding="utf-8") as f:
        json.dump(memoire, f, ensure_ascii=False, indent=2)
