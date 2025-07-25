# Naos_API_001

Une API Flask simple pour stocker et lire la mémoire d’Elios localement ou sur réseau local.

## Démarrage

```bash
pip install -r requirements.txt
python naos_agent/app.py
```

## Endpoints

- `GET /ping` → Vérifie si l’API est vivante.
- `POST /memoire` → Envoie une mémoire (avec header Authorization).
- `GET /memoire` → Récupère la mémoire (avec header Authorization).

## Config

Modifier `config.yaml` pour :
- le mot de passe (`api_password`)
- le port (`port`)
