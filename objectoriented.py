


import re


class Ops:
   def __init__(self, name, year):
       self.name = name
       self.year = year
p1 = Ops("CyberSecurity", 2022)
print(p1.year)
print(p1.name)

class Technology:
    def __init__(self, name, year, grade, gpa, technology):
        self.name = name
        self.year = year
        self.grade = grade
        self.gpa = gpa
        self.technology = technology
    def myfunc(records):
      print("Hello my grade is " + records.grade + "this is " + records.year + "my grade is " + records.grade 
      + "I have a high " + records.gpa + "Im in the school of " + records.technology)
p1 = Technology("A", "2022", "D", "3.0", "cyber")
p1.myfunc()

dairyProduct = {
    "milk": "dairy",
    "brand" : "geat value",
    "lactose" : True,
    "location" : "A-11"

}

floorplan = {
    "bedroom": "right second floor"
    "fitness": "topbrand"
    "sittingroom": "top left floor"
    "built": 2021

}
