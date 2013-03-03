import xml.etree.ElementTree as ET
tree = ET.parse('subject.xml')
root = tree.getroot()                            # "Holen" des Wurzel-Elements der XML-Datei


for country in root.findall('CONCEPT'):          # Jeden Root finden

#    if country.find('continent').text=='Africa': # Zu einem Staat den Kontinent finden
#        print country.find('capital').text       # Zum Staat die Hauptstadt finden

# an der Stelle muessen wir uns noch ueberlegen, was wir mit den Daten anfangen wollen.