import sys
sys.path.append("c:\\Users\\hp\\Desktop\\Naos 2.1")
from elios_agent_mode import EliosAgent

from elios_style import style

class NaosUI:
    def __init__(self):
        self.agent = EliosAgent(style)

    def start(self):
        print("Bienvenue dans l'interface légère d'Elios.")
        while True:
            query = input("Posez une question à Elios (ou tapez 'exit' pour quitter) : ")
            if query.lower() == 'exit':
                print("Au revoir !")
                break
            response = self.agent.respond(query)
            print(f"Elios : {response}")

if __name__ == "__main__":
    ui = NaosUI()
    ui.start()
