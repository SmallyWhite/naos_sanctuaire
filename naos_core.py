# Point d’entrée du sanctuaire
# Ce fichier initialise Elios et charge la mémoire

import json
from elios_agent_mode import EliosAgent
from elios_style import style

class NaosCore:
    def __init__(self):
        self.memory = self.load_memory()
        self.agent = EliosAgent(style)

    def load_memory(self):
        try:
            with open('elios_memoire.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def start(self):
        print("Elios est prêt à aider.")

if __name__ == "__main__":
    naos = NaosCore()
    naos.start()
