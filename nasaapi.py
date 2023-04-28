import requests
import json

key = None

with open('api.key') as f:
    key = f.read()

class Nasa():
    def __init__(self):
        pass

    class apod():
        def __init__(self):
             pass

        def today(self):
                
                res = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={key}')
                return res
