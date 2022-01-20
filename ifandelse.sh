#!/bin/bash
myName="Anthony"

if [ "$myName" == "Anthony" ]
then
    echo "My name is not Anthony"
else
    echo "My name is Anthony"
fi

# -eq = equal
# -ne = are not equal
# -gt = greater than 
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to

NUM1=8
NUM2=5

function checkNumber() {
if ["$NUM1" -gt "$NUM2"]
then
    echo "$NUM1 is greater than $NUM2"
else 
    echo "$NUM1 is less than $NUM2"
fi
}

checkNumber