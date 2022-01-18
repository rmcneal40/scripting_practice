#!/bin/bash

#create a variable that holds the value of the day
HywaManager="Jason"
HywbManager="Brian"
HywcManager="Keith"


# need to create three arrays that holds the a work order
HywReplacements=("patch holes" "refresh paint" "fix rails, create signs")
StreetTickets=("replace blacktop" "fix signs" "create notes")
ParkWork=("Swing replace" "bench work" "remodel fountain" )


function Jason() {
    for i in "${HywReplacements[@]}"
    do
        echo "Message for $HywaManager to assign the following replacements $i"
    done
}
Jason
function Brian() {
    for i in "${StreetTickets[@]}"
    do
        echo "Note for $HywbManager to carry out the orders of $i"
    done
}
Brian
function Keith() {
    for i in "${HywcManger[@]}"
    do
        echo "Give this to $HywcManager to report to these directions $i"
    done
}
Keith


function repairEvents() {
    if [ "$HywaManager" == "Jason" ]
    then
        Jason
    else
        Brian
    fi
}
repairEvents