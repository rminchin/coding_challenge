# import modules
import argparse
import csv
import random
import haversine as hs
import tabulate

# define variables
places = {}
places_iterate = 0
places_to_use = {}
pairs = {}
distances = []

# open the csv file and add data to list
with open('places.csv', mode='r') as file:
    csvFile = csv.reader(file)

    for lines in csvFile:
        if 'Name' not in lines[0]:
            places[lines[0]] = lines[1] + "," + lines[2]

# configure argparse
parser = argparse.ArgumentParser(description="Air distance program")
parser.add_argument("-n", nargs='?', type=int, help="Optional integer, n, to determine number of places to select")
args = parser.parse_args()

# if n argument provided, ensure validity and use input provided
# if not, use entire dataset provided in places.csv
if args.n is not None:
    if args.n < 2:
        places_iterate = 2
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
        place = key, val = random.choice(list(places.items()))
        places_to_use[place[0]] = place[1]
        places.pop(place[0])

places_names = list(places_to_use.keys())

# calculate pairs and distances
x = 0
y = 1
total = 0
while True:
    try:
        place1_name = places_names[x]
    except IndexError:
        x += 1
        y = x + 1
        try:
            place1_name = places_names[x]
        except IndexError:
            # reached end of list
            break

    try:
        place2_name = places_names[y]
    except IndexError:
        x += 1
        y = x + 1
        try:
            place2_name = places_names[x]
        except IndexError:
            # reached end of list
            break

    # lat, long pairs for haversine function
    place1_loc = (float(places_to_use[place1_name].split(",")[0]), float(places_to_use[place1_name].split(",")[1]))
    place2_loc = (float(places_to_use[place2_name].split(",")[0]), float(places_to_use[place2_name].split(",")[1]))

    # calculate haversine distance between the two points
    distance = hs.haversine(place1_loc, place2_loc)
    if distance not in distances:
        pairs[distance] = place1_name + "-" + place2_name
        distances.append(distance)
        total += distance

    # next pair
    y += 1

# sort pairs into order of distance
pairs_in_order = sorted(pairs)
sorted_dict = {}
for i in pairs_in_order:
    sorted_dict[i] = pairs[i]

# data calculation
# data is rounded for output but kept precise for calculations
headers = ['Place 1', 'Place 2', 'Distance (km)']
data = []
average = total / len(sorted_dict)
closest_distance = 999999999999
closest_pair = ''
for key, value in sorted_dict.items():
    data.append([value.split("-")[0], value.split("-")[1], round(key, 3)])
    if abs(key - average) < closest_distance:
        closest_distance = abs(key - average)
        closest_pair = value

# data output
print(tabulate.tabulate(data, headers, tablefmt='presto'))
print()
print("Average distance: " + str(round(average, 3)) + "km, Closest pair: " + closest_pair + " " +
      str(round(closest_distance, 3)) + " km")
