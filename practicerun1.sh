#!/bin/bash
#Main
# -eq = equal
# -ne = are not equal
# -gt = greater than 
# -ge = greater or equal to
# -lt = less than
# -le = less than or equal to
# >= (Greater than or equal to)
# <= (Less than or equalk to)
# > (Greater)
# < (Less)
# == (comparison)
# % (Remainder)
# * (Multiply)
# && = must include
# || = or
# -v = option BASH shell will echo every command before substituting the values of arguments and variables. In –v option Unix will print each line as it reads.
# -x = –x option BASH shell will echo the commands like for, select, case etc. after substituting the arguments and variables. So it will be an expanded form of 
# the command that shows all the actions of the script. It is very useful for debugging a shell script. 
# -z = The -z flag causes test to check whether a string is empty. Returns true if the string is empty, false if it contains something.
# nc = NetCat to check if the port is listening on linux. 

#Here is a mini challenge to engage where you are. Do not be scared to try things out to see if it works or not. Break it to fix it! 

# 1.) Echo out "Hello, what is your name?"
# 2.) Create a user input with a variable "name".
# 3.) Echo out "Nice to meet you _____" The blank is where your name would appear.
# 4.) Echo out "Enter a number 1 - 100".
# 5.) Create a user input with variable "number"
# 6.) Create a If statements to accept the argument, if "number" is less then 100, printf out "_____ is less than 100" and else will provide the argument, 
# if "number" is greater then 100, printf out "_____ is greater than 100"

echo "Hello, what is your name?"
read UserInput

echo "Nice to meet you Kurtis"
echo "Enter a number 1 - 100"
read UserInput


function checkNumber() {
if [ $Number -gt 100 ]
then 
    echo "The number is -lt than 100"
else
    echo "The number is grader than 100"
fi
}
checkNumber



#Example of If and Else Statement:

#if [ $number -lt 100 ]; then
printf "$number is less than 100\n"

