#!/bin/bash
function print_something () {
  echo Hello I am a function
}
print_something
print_something
#function using premeters to show output.
function greet() {
    echo "Hello, I am $1 and I am $2. I just ate $3 and I am full $4"
}
greet "Kurtis" "42" "Subway" "anthony"
#simple function to add
function recepitCalulator() {
totalSum=$(( $1 + $2 ))
echo "Sum is: $totalSum"
}
recepitCalulator 23 5
# Creating a variable called myName
myName="Kurtis"
#function to call the varable
function show_Name() {
   echo $myName
}
#Main
show_Name