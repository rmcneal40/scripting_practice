M# Today we will be doing a Array challenge in class I have came up with. This will refresh your first ops challenge well as learn array and functions.
# Class Challenge: Bob goes shopping on Monday, Wednesday, and Friday.
# Monday, he has grocery list of:
# "GroundBeef" "Milk" "Eggs" "Cereal" "Frozen Pizza" "Rice" "Ramen" "Chicken" "Dog Food" "Cat Food" "Spaghetti Sauce" "Apple Sauce"
# Wednesday, he has clothes shopping list of:
# "pants" "Jacket" "Scarf" "boots" "Hat"
# And Friday, Electronic shopping list of:
# "TV" "PS5" "motherboard" "CPU" "RAM"
# Bob wants to be able to create a txt file according to the shopping day just by plugging in the day and running the script.
# It is your task to help Bob out!
# Think about it and lets make this happen today!
#!/bin/bash

#create a variable that holds the value of the day

day="Monday"

# need to create three arrays that holds the grociry list, and need to make clothing list, and a electronic list
Grocerylist=("GroundBeef" "Milk" "Eggs" "Cereal" "Frozen Pizza" "Rice")
Clothinglist=("hat" "scarf" "shoes" "socks" "boots")
Electronics=("PC" "dvd" "radio" "usb")

#I need to create funtions for mon, wed and fri. need to creat a textfile within the function.

function Monday() {
    for i in "${Grocerylist[@]}"
    do
        echo $i
    done > robert.txt
}
function Tuesday() {
    for i in "${Clothinglist}"
    do
        echo $i 
        done > mike.txt
}
function Friday() {
    for i in "${Electronics}"
    do
        echo $i 
        done > tony.txt
}


#this is where if and else statement goes
function shoppinglist() {
    if [ "$day" == "Monday" ]
    then
        Monday 
    elif [ "$day" == "Tuesday" ]
    then
        Tuesday
    else
        Friday
    fi 

}
shoppinglist 