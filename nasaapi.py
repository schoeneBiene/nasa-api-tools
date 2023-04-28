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
    class earth(): # Refuses to work because it couldnt find anything, even on the one on the nasa api example page bruh
         def __init__(self):
              pass
         def Imagery(lat, lin):
              headers = {"lat":lat, "lon": lin, "api_key": key}
              print(headers)
              res = requests.get("https://api.nasa.gov/planetary/earth/imagery",headers)
              return res
