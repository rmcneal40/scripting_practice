#!/bin/bash

echo "What side of the building are you located?"
read rightSide
echo "If working on the right side of the building then your in c class"
echo "All left side students will be in class bronco"
echo "Whos at the bottom building"
read leftSide
echo "You will have to wait until next term"
echo "Who does not understand?"
read bottom
echo Speak to advisor



read bottom 

if [ $rightSide ] ;
then
    echo "If working on the right side of the building then your in voyager class"
else [ $leftSide ] ;

    echo "All left side students will be in class bronco"
else [ $bottom ] ;
then
    echo "You will have to wait util next term"
else 
then
    echo "Speak to advisor"
fi
