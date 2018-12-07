import random
from datetime import datetime

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

class VkUser(Human):

    def __init__(self,BD,gender,firstname,vk,lastname = '',**kwargs): 
        super().__init__(BD,gender,firstname,lastname = '',**kwargs)
        self.vk = ''
        for i in vk:
            if i>"0" and i<"9":
                self.vk += i

    def link(self):
        return("https://vk.com/id"+self.vk)

a = VkUser("1999-02-22", "female", "Ann", "id44700001", city = "Krsk")
b = VkUser("1984-03-12", "male", "Din", "id33800002", city = "SPB")
print(a, a.link(), a.age(), b, b.gender, b.arg, b.link(), sep = "\n")
