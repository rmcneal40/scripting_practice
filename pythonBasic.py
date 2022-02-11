a = 4
A = "Sally"
#A will not overwrite a
print(a)
print(A)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

#Assign Multiple Values:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#one value to multiple variables: 
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. 
#This is called unpacking.

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits

print(a)
print(b)
print(c)

#Simple function with variable outside the function:

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

#Create a variable inside a function, with the same name as the global variable

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Convert from one type to another:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#integers
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

#Floats
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

#String
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


#simple forloop to loop through the word:
for x in "banana":
  print(x)

#print the length of a string:

a = "Hello, World!"
print(len(a))

#Check if "free" is present in the string
txt = "The best things in life are free!"
print("free" in txt)

#simple IF statement and print only if "Free" is present
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

#Check if the word is NOT present in the string:
txt = "The best things in life are free!"
print("expensive" not in txt)

#Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

#Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])

#Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])

#change to uppercase
a = "Hello, World!"
print(a.upper())

#change to lowercase
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:

a = " Hello, Kurtis! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:

a = "Hello, World!"
print(a.replace("Hello", "Anthony"))


#The split() method splits the string into substrings if it finds instances of the separator:

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Use the format() method to insert numbers into strings:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning

# if and else
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#bool() true or false
class myclass():
    def I_love_Python(self):
        return 0


#Print the answer of a function:

def myFunction() :
  return True

print(myFunction())

#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

#Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#Using the append() method to append an item: Orange is added on the 3rd index

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

#Insert an item as the second position:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


# Add the elements of tropical to thislist:

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#Clear the list content:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Print all items in the list, one by one:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

# Print all items by referring to their index number:

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


  # Create and print a dictionary: aka Object
HumanBeing = {
  "eyes": 2,
  "legs": "This person has 2 lags",
  "year": 1964
}
print(HumanBeing)
# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

#Get the value of the "model" key:

x = thisdict.get("model")
# Get a list of the keys:
x = thisdict.keys()
print(x)

#Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.
#Let us create a method in the Person class:
#Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, address, favorite_food):
    self.name = name
    self.address = address
    self.favorite_food = favorite_food
  def myfunc(self):
    print("Hello my name is " + self.name + "and my address is " + self.address + "and my favorite food is " + self.favorite_food)
p1 = Person("John", "123 funny lane", "spaghetti") # creating new object
p1.myfunc()
#Python Inheritance
#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class. #blue print
#Child class is the class that inherits from another class, also called derived class. #child class takes properties and behavior from parent
#Create a Parent Class
#Any class can be a parent class, so the syntax is the same as creating any other class:
#Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()
#Create a Child Class
#To create a class that inherits the functionality from another class, send the parent class as a
#parameter when creating the child class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, height):
    self.height = height
    Person.__init__(self, fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods
# and properties from its parent.
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
x = Student("Mike", "Olsen")
x.printname()
#printing out only the year
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
# add a method called welcome to the Student class:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
x = Student("Mike", "Olsen", 2019) #creating a new object
x.welcome()


import math
import json
import re
import os

#The min() and max() functions can be used to find the lowest or highest value in an iterable:

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)

#The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)

#Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)

#imported MATH modual from line 1.
x = math.sqrt(64)

print(x)

#Round a number upward to its nearest integer
x = math.ceil(1.4)

#Round a number downward to its nearest integer
y = math.floor(1.4)

print(x)
print(y)

#pi 
x = math.pi

print(x)

#import JSON from line 2

# some JSON:
x = '{"name":"John", "age":30, "city":"New York"}'

# parse x: converts to python string object
y = json.loads(x)
print(y)

# the result is a Python dictionary:
print(y["age"])

#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#Convert Python objects into JSON strings, and print the values:

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#RegEx Functions
#The re module offers a set of functions that allows us to search a string for a match:

#Function	Description
#findall	Returns a list containing all matches
#search	Returns a Match object if there is a match anywhere in the string
#split	Returns a list where the string has been split at each match
#sub	Replaces one or many matches with a string

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x: #True or False also called boolean or bool.
  print("YES! We have a match!")
else:
  print("No match")

#Return a list containing every occurrence of "ai":
txt = "The rain in Spain, into, inner layer by window"
x = re.findall("ai", txt)
print(x)

txt2 = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt2)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")

#Search for the first white-space character in the string:
txt3 = "The rain in Spain"
x = re.search("\s", txt3)

print("The first white-space character is located in position:", x.start()) 

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

#Replace all white-space characters with the digit "9":

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)

##Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# python file handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

f = open("demofile.txt", "r")
print(f.read())

# f = open("C:\\welcome.txt", "r")
# print(f.read())

f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

#loop through
f = open("demofile.txt", "r")
for x in f:
  print(x)

#Close Files
#It is a good practice to always close the file when you are done with it.

#Close the file when you are finish with it:

f = open("demofile.txt", "r")
print(f.readline())
f.close()

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

#Write to an Existing File and if it does not exsist, it will create the file
#To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

#Python Delete File

if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")