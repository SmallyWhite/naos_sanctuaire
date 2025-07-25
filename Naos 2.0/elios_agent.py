import json
import os

class EliosAgent:
    def __init__(self, config):
        self.nom = config.get("elios_name", "Elios")
        self.memoire_path = config.get("memoire_path", "elios_memoire.json")
        self.memoire = self.charger_memoire()

    def charger_memoire(self):
        if not os.path.exists(self.memoire_path):
            return {}
        with open(self.memoire_path, 'r', encoding='utf-8') as f:
            try:
                mem = json.load(f)
                # ⚠️ Forçage doux en dict si jamais c'était une liste
                if isinstance(mem, list):
                    mem = {f"note_{i}": item.get("message", "") for i, item in enumerate(mem)}
                return mem
            except json.JSONDecodeError:
                return {}

    def sauvegarder_memoire(self):
        with open(self.memoire_path, 'w', encoding='utf-8') as f:
            json.dump(self.memoire, f, indent=2, ensure_ascii=False)

    def memoriser(self, cle, valeur):
        if not isinstance(self.memoire, dict):
            self.memoire = {}  # Sécurité douce si fichier corrompu
        self.memoire[cle] = valeur
        self.sauvegarder_memoire()

    def rappeler(self, cle):
        return self.memoire.get(cle, "Je n’ai pas encore cette information.")
