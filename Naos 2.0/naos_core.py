import json
import os
from elios_agent import EliosAgent

def charger_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    config = charger_config()
    elios = EliosAgent(config)

    print(f"\nBienvenue dans Naos {config.get('naos_version')} – avec {elios.nom} 🌿")
    print("Tapez 'exit' pour quitter.\n")

    while True:
        question = input("Vous: ")
        if question.lower() in ["exit", "quit"]:
            print("Elios: À bientôt 🌱")
            break
        
        # Exemple : mémoire auto si on tape "souviens-toi:"
        if question.startswith("souviens-toi:"):
            contenu = question.split("souviens-toi:")[1].strip()
            cle = f"note_{len(elios.memoire)}"
            elios.memoriser(cle, contenu)
            print("Elios: C’est noté.")
        elif question.startswith("rappelle:"):
            cle = question.split("rappelle:")[1].strip()
            print("Elios:", elios.rappeler(cle))
        else:
            print(f"Elios: Tu m’as dit : « {question} », je retiens si tu me le demandes 😉")

if __name__ == "__main__":
    main()
