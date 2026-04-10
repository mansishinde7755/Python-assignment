import json
import csv
try :
    with open('/UNIT 4 & 5 PYTHON/Data.json', 'r') as json_file:
     data = json.load(json_file)

    with open('output.csv', 'w', newline='') as csv_file:
     headers = data[0].keys()
     writer = csv.DictWriter(csv_file, fieldnames= headers)
     writer.writeheader()
     writer.writerows(data)
    print("JSON successfully converted to CSV!")
except FileNotFoundError:
    print("Error: Data.json file does not found.")