import nasaapi
import argparse
import path
import os
import misc

nasa = nasaapi.Nasa()

tasks = ["apod","earth","debug"]


parser = argparse.ArgumentParser("Nasa API")

parser.add_argument("-t","--task", type=str, help="Defines what API the programm should access.", required=True)
parser.add_argument("-o", "--out", type=str, help="Defines the output for images. Ex.: image.png", required=False)
parser.add_argument("-d", "--date",type=str, help="The date used for Earth, YYYY-MM-DD",required=False)
parser.add_argument("-l","--location", type=float, nargs=2, help="Location in lat and lon, Ex: -l lat lon")
# parser.add_argument("-s","-suppress", type=None, help="Takes no extra args, when provided will suppress the information printed to the console excluding errors.")
# Above removed due to not working.


args = parser.parse_args()
task = args.task
exists = False

for x in tasks:
    if task.lower() == x:
        exists = True

if exists == False:
    print("[ERR] Task specified does not exist!")
    exit()

if task.lower() == "apod":
    doout = False
    if args.out:
       doout = True
    
    info = nasa.apod().today().json()
    

    
    print(f'Title: {info["title"]}')
    print(f'Explanation: {info["explanation"]}')

    if doout == True:
        result = misc.saveImg(info["url"], args.out)
        if result == 3:
            print("File specified already exists!")


# Refuses to work

# if task.lower() == "earth":
#     doout = False
#     if args.out and args.location:
#        doout = True

#     if doout == False:
#         print("[ERR] No out/location/date provided.")
    
#     img = nasa.earth.Imagery(args.location[0],args.location[1]).content
#     result = misc.saveContent(img, args.out)

#     if result == 3:
#         print("File specified already exists!")

# if task.lower() == 'debug':
#     print(args.location)