import random
from datetime import datetime, timedelta
import xml.etree.ElementTree as ET
tree = ET.parse("infos/earth.xml")
earth = tree.getroot()

class Human(object):

    def __init__(self,BD,gender,firstname,lastname = '',**kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.BD = BD
        self.gender = gender
        self.arg = kwargs

    def __str__(self):
        return(self.firstname+" "+self.lastname)

    def age(self):
        now = datetime.now()
        BD = datetime.strptime(self.BD,"%Y-%m-%d")
        age = now.year - BD.year
        if now.month<BD.month or(now.month==BD.month and now.day<=BD.day):
            age -= 1
        return(age)

people = []
for hum in earth:
    d={}
    LN=""
    for elem in hum:
        if elem.find("*") is None:
            if elem.tag == "BirthDate":
                BD = elem.text
            elif elem.tag == "FirstName":
                FN = elem.text
            elif elem.tag == "LastName":
                LN = elem.text
            else:
                d[elem.tag]=elem.text
        else:
            for el in elem:
                d[el.tag]=el.text
    people.append(Human(BD,random.choice(["male","female"]),FN,LN,vk = d["vk"],City = d["City"]))
