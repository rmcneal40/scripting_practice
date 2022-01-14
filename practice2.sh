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
year="TwentyTwenty"

# need to create three arrays that holds the grociry list, and need to make clothing list, and a electronic list
Operations=("KneeReplacement" "HipSurgery" "BrainScan" "FaceLift" "FootScan" "Tlift")
Accomplishments=("Graduation" "NewCar" "NewHouse" "NewBorn" "Married")
Diary=("Goals" "Morals" "Values")

#I need to create funtions for mon, wed and fri. need to creat a textfile within the function.
function TwentyTwenty() {
    for i in "${Operations[@]}"
    do
        echo "In the year 2016 Ive had multiple surgerys as listed $i"
    done
}

function TwentySeventeen() {
    for i in "${Accomplishments[@]}"
    do
        echo "I had a wonderful year in 2017 and these are my accomp... $i"
    done
}

function thirty() {
    for i in ${Diary[@]}
    do
        echo "There were no bad things written in my diary 2020, but... $i"
    done
}
#thirty  (test worked)!!!!

function lifeEvents() {
    if [ "$year" == "TwentyTwenty" ]
    then
        TwentyTwenty
    elif ["$year" == "TwentySeventeen" ]
    then
        TwentySeventeen
    else
        thirty
    fi
    
}
lifeEvents






















# this is where if and else statement goes



