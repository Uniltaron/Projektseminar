import re
import csv
import json

textfile = "lorem.txt"
with open(textfile, "r") as text:
    content = text.read()

# CSV-Export
with open("lorem_csv.csv", "w") as csv_output:
    writer = csv.writer(csv_output, delimiter=';')
    for word in d:
        writer.writerow([word, d[word]])

# JSON-Export
with open("lorem_json.json", "w") as json_output:
    json.dump(d, json_output)

# JSON-Import
with open("lorem_json.json", "r") as json_input:
    data = json.load(json_input)

print data, type(data)
