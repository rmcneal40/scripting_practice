#Bob is back at it again! Now he needs us to script something that if 
#user inserts between two to 5, it will print out "Valid Number" and 
#"your number is ___". 
#And if the user input is not between 2 and 5, it will print out "not valid! 
#Please enter another Number."

# 1.) create a function and give it a name.
# 2.) inside the function, put a read with a varible "number"
# 3.) create an if and else statement with the argument like this. 
#if the read variable "number" is greater than or equal to two AND! "number" is less than or 
# equal to 5, iit will echo out "valid number" Else, it will echo out "not a valid number, try again". 
# 4.) Right below the last echo from #3, call the function from instruction #1 and close the if and else statement.

# ***Please note***: Do not put instruction #5, #6, #7 in the function but outside the function.

# 5.) echo out "insert number" outside the function. 
# 6.) call the function from instruction #1
# 7.) echo out "your number is _____." and the blank being the user input number.  
#/bin/bash
echo "insert number"

function bobsBack() {
read number
if ((number >= 2 && number <= 5)); 
then 
    echo "valid number"
else 
    echo "not a valid number, try again"
    bobsBack        
fi
}


bobsBack
echo "your number is  $number"

