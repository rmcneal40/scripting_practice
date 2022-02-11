#Excercise 1




#Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#Create a new object called modelX and pass the parent properties and (240, 18). 240 being the max speed and 18 being mileage

modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)

#Create a Vehicle class without any variables and methods

#ANSWER
class Bus(Vehicle):
    pass

#Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.

#Expected Output:
#Vehicle Name: School Volvo Speed: 180 Mileage: 12

#Use the code below to start your exercise

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

#ANSWER
School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)



#Exercise 3

#Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
class Vehicle:
    def __init__(self, name, seating_capacity):
        self.name = name
        self.seating_capacity = seating_capacity(50)

    
#Use the following code for your parent Vehicle class.

#Expected Output:

#The seating capacity of a bus is 50 passengers

#Hint: First, use method overriding. 
# Next, use default method argument in the seating_capacity() method definition of a bus class.

#Use the following code for your parent Vehicle class.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"




#Answer To Exercise 3

#Use the following code for your parent Vehicle class.
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
#f-string is a easy way to print out a string.
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

#ANSWER
class Bus(Vehicle):
    # assign default value to capacity
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

