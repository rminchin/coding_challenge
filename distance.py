# import modules
import argparse
import csv
import random

# define variables
places = []
places_iterate = 0
places_to_use = []

# open the csv file and add data to list
with open('places.csv', mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        if 'Name' not in lines[0]:
            places.append(lines[0] + " " + lines[1] + " " + lines[2])

# configure argparse
parser = argparse.ArgumentParser(description="Air distance program")
parser.add_argument("-n", nargs='?', type=int, help="Optional integer, n, to determine number of places to select")
args = parser.parse_args()

# if n argument provided, ensure validity and use input provided
# if not, use entire dataset provided in places.csv
if args.n is not None:
    if args.n < 0:
        places_iterate = 0
    elif args.n > 10:
        places_iterate = 10
    else:
        places_iterate = args.n
else:
    places_iterate = 10

# generate places to use for this run
if places_iterate == 10:
    places_to_use = places
else:
    for i in range(places_iterate):
        place = random.choice(places)
        places_to_use.append(place)
        places.remove(place)

print(places_to_use)