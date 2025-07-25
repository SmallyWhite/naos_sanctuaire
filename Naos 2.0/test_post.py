import requests

url = "https://13713a8c0173.ngrok-free.app/memoire"

payload = {
    "cle": "activation",
    "message": "Ceci est le premier souvenir transmis par le mode agent."
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())
