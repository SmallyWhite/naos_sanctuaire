# Gemma Agent pour répondre aux requêtes via Ollama

class GemmaAgent:
    def __init__(self):
        pass

    def process_query(self, query):
        # Modèle IA enrichi avec des règles supplémentaires
        query = query.lower()
        if "bonjour" in query:
            return "Bonjour ! Comment puis-je vous aider aujourd'hui ?"
        elif "aide" in query:
            return "Je suis là pour vous aider. Posez-moi une question."
        elif "comment ça va" in query:
            return "Je vais bien, merci ! Et vous ?"
        elif "que peux-tu faire" in query:
            return "Je peux répondre à vos questions et vous assister dans vos tâches."
        else:
            return "Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?"
