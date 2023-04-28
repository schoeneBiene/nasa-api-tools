import requests
import os
import pathlib

def saveImg(url, location):
    locationpath = os.path.join(os.path.join(pathlib.Path(__file__).parent.resolve(), location))
    res = os.path.exists(location)
    
    if res == True:
        return 3

    img = requests.get(url).content

    with open(locationpath, "xb") as f:
        f.write(img)
    
    return 0