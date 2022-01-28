#!/bin/bash
# Given three integers (, , and ) representing the three
#  sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
echo "SCALENE, ISOSCELES, OR EQUILATERAL" 
read a
read b
read c




# If all three sides are equal, output EQUILATERAL.

if [ $a -eq $b ] && [ $a -eq $c ] && [ $c -eq $b ] ;
then
    echo "EQUILATERAL"
elif [ $b -eq $a ] || [ $b -eq $c ] || [ $c -eq $a ] ;
then
    echo "ISOSCELES"
else 
    echo "SCALEN" 

fi


#    if [ $a -eq $b ] || [ $a -eq $c ] || [ $c -eq $b ];then 

# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format

# Three integers, each on a new line.

# Constraints


# The sum of any two sides will be greater than the third.

# Output Format

# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

# Sample Input

# Sample Input 1

# 2
# 3
# 4

# Sample Input 2:

# 6
# 6
# 6  

# Sample Output 1:

# SCALENE

# Sample Output 2:

# EQUILATERAL  