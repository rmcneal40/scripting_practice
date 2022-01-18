#!/bin/bash

echo "please inter a number"
#read is user input
# numberone=user input.

read numberone 
echo "please inter second number"
read numbertwo

function add() {
    sum=$((numberone + numbertwo))
        echo $sum
 
}
add



function subtact() {
    sum=$((numbertwo - numberone))
        echo $sum
}
subtact

function divide() {
    sum=$((numberone / numbertwo))
        echo $sum
}
divide

function ReMainder() {
    sum=$((numberone % numbertwo))
        echo $sum
}
ReMainder