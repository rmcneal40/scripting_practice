#!/bin/bash
# Script:                      
# Author:                      
# Date of latest revision:      
# Purpose:                      
# Declare global variables
files=("f1.txt" "f2.txt" "f3.txt" "f4.txt" "f5.txt")
# Declare functions
# Main
echo ${files[4]}
echo ${files[3]}
echo ${files[2]}
echo ${files[1]}
echo ${files[0]}
#Array Example 2
my_array=(foo bar baz)
for index in "${!my_array[@]}";
do
    echo "$index";
done
#Array Example 3
array1[0]=one
array1[1]=1
echo ${array1[0]}
echo ${array1[1]}
array2=( one two three )
echo ${array2[0]}
echo ${array2[2]}
array3=( [9]=nine [11]=11 )
echo ${array3[9]}
echo ${array3[11]}
read -a array4
fr i in "${array4[@]}"
do
    echo $i
done
