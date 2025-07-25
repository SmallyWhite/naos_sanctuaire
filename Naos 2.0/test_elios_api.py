import requests

data = {"message": "Souviens-toi que Stephen m’a tout confié ce matin."}

response = requests.post("http://localhost:5000/", json=data)

print("Réponse brute :", response.text)
print("Elios répond :", response.json()["response"])
