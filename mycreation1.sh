#!/bin/bash

# My variable for loop practice 1/12/2022

# My variables
myNameIs=Robert
myWorkIs=Walmart
myCityIs=StLouis
myStateIs=Mo
# My Arrays
myInfo=("City" "State" "Place of work" "My name")
function City() {
    echo "The city I live in is StLouis"
}
City

function State() {
    echo "The state that I reside in is Mo"
}
State

function WorkPlace() {
    echo "My place of work is Walmart"
}
WorkPlace

for Myinformation in "${myInfo[@]}"
do
    echo $MyCityIs "If my city is $myCityIs and my state is $myStateIs[$Myinformation] then 
    my name is $myNameIs, plus $myInfo,
    which means I work at $myWorkIs"
done