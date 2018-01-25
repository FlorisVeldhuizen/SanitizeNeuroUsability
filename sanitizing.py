import json
import csv
from pprint import pprint

#load the json data
with open('data_17.1.18.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

#open a csv file for writing
csv_data = open('SanitizedData.csv','w',newline='')

#create a csv writer
csvwriter = csv.writer(csv_data,delimiter=';')

header = ("id","name","level","clicks","distance to perfect","total errors","time","verwirrend","voraussagbar","praktisch","phantasielos","minderwertig","lahm","hässlich","gut","einfach","age","course","edu")
csvwriter.writerow(header)

keylist = data.keys()
for key in keylist:
    keydata = list()
    keydata.append(data[key]['result']['id'])
    keydata.append(data[key]['result']['name'])
    keydata.append(data[key]['result']['level'])
    keydata.append(data[key]['result']['total']['clicks'])
    keydata.append(data[key]['result']['total']['distanceToPerfectClicks'])
    keydata.append(data[key]['result']['total']['totalAbsoluteLetterError'])
    keydata.append(data[key]['result']['total']['time'])
    keydata.append(data[key]['result']['verwirrend'])
    keydata.append(data[key]['result']['voraussagbar'])
    keydata.append(data[key]['result']['praktisch'])
    keydata.append(data[key]['result']['phantasielos'])
    keydata.append(data[key]['result']['minderwertig'])
    keydata.append(data[key]['result']['lahm'])
    keydata.append(data[key]['result']['hässlich'])
    keydata.append(data[key]['result']['gut'])
    keydata.append(data[key]['result']['einfach'])
    keydata.append(data[key]['result']['age'])
    keydata.append(data[key]['result']['course'])
    keydata.append(data[key]['result']['edu'])
    csvwriter.writerow(keydata)

