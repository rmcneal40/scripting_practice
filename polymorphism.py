#Polymorphism with Inheritance
#Expected Output - 

# Details: Car x1 Red 20000
# Car max speed is 240
# Car change 7 gear

# Details: Truck x1 white 75000
# Vehicle max speed is 150
# Vehicle change 6 gear

#POLY means "many"
#Morph means "forms"
#polymorth = it can take many forms. 

class Vehicle:

    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def show(self):
        print('Details:', self.name, self.color, self.price)

    def max_speed(self):
        print('Vehicle max speed is 150')

    def change_gear(self):
        print('Vehicle change 6 gear')


# inherit from vehicle class
class Car(Vehicle):
    def max_speed(self):
        print('Car max speed is 240')

    def change_gear(self):
        print('Car change 7 gear')


# Car Object
car = Car('Car x1', 'Red', 20000)
car.show()
# calls methods from Car class
car.max_speed()
car.change_gear()

# Vehicle Object
vehicle = Vehicle('Truck x1', 'white', 75000)
vehicle.show()
# calls method from a Vehicle class
vehicle.max_speed()
vehicle.change_gear()

# As you can see, due to polymorphism, the Python interpreter recognizes that the max_speed() 
# and change_gear() methods are overridden for the car object. So, it uses the one defined in the child class (Car)

# On the other hand, the show() method isn't overridden in the Car class, so it is used from the Vehicle class.