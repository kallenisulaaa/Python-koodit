import requests as rq

pyyntö = 'https://api.chucknorris.io/jokes/random'
vitsi = rq.get(pyyntö).json()
print(vitsi["value"])