import csv, sys
	filname='anyfile.csv'
	with open ('filname.csv', 'r') as data: 
		reader = csv.reader(data, delimiter=';')
		 try:
        	for row in reader:
            	print row
   		 except csv.Error as error:
        	sys.exit('file %s, line %d: %s' % (filename, reader.line_num, error))

			
	with open('new_some.csv', 'w') as new_data:
    writer = csv.writer(new_data, delimiter=';')
    writer.writerows(list_data)
    
    
import json
	with open("some.json", "r") as json_input:
    data = json.load(json_input)
		print data, type(data)
	with open("new_some.json", "w") as json_output:
    json.dump(new_data, json_output)		
		
		
		
		
import xml.etree.ElementTree as ET
tree = ET.parse('some.xml')
root = tree.getroot() 
