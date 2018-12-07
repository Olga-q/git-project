import xml.etree.ElementTree as ET
tree = ET.parse("infos/earth.xml")
earth = tree.getroot()
l=[]
for human in earth:
    d={}
    for elem in human:
        if elem.find("*") is None:
            d[elem.tag]=elem.text
        else:
            for el in elem:
                d[el.tag]=el.text
    l.append(d)
for a in l:
    for b in a:
        print (b,":",a[b])


