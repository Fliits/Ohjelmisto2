import requests
import json

syöte = input("Anna paikkakunta: ").capitalize()

paikka = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={syöte}&limit=1&appid=3f2d9ed64dd98f53f5f43a0736069789").json()

# print(paikka)

kunta = paikka[0]

leveys = kunta["lat"]
pituus = kunta["lon"]

vastaus = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={leveys}&lon={pituus}&appid=3f2d9ed64dd98f53f5f43a0736069789&units=metric").json()

# print(vastaus)

#sää = vastaus[1]
#lämpö = vastaus[3]

print(vastaus["weather"][0]["description"],",", vastaus["main"]["temp"], "Celsiusta")