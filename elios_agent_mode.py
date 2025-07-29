# Agent principal local (Gemma ou Phi)

from engine.gemma_agent import GemmaAgent

class EliosAgent:
    def __init__(self, style):
        self.style = style
        self.gemma = GemmaAgent()

    def respond(self, query):
        # Utilise Gemma pour traiter la requête
        return self.gemma.process_query(query)
