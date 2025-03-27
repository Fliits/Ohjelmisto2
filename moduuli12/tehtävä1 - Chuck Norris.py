import requests

# pyyntö = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get("https://api.chucknorris.io/jokes/random").json()
print(vastaus["value"])