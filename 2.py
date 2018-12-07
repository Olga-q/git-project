import xml.etree.ElementTree as ET
tree = ET.parse("infos/earth.xml")
earth = tree.getroot()

for human in earth:
    print(human.find("FirstName").text,end = " ")
    if human.find("LastName") is not None:
        print(human.find("LastName").text)
    else:
        print()

city=set()
for human in earth:
    c = human.find("Address").find("City").text
    city.add(c)
    print (c)

print(len(earth))
print(len(city))
