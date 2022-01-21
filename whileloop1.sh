# The case line itself is always of the same format, and it means that we are testing the value of the variable INPUT_STRING.

# The options we understand are then listed and followed by a right bracket, as hello) and bye).
# This means that if INPUT_STRING matches hello then that section of code is executed, up to the double semicolon.
# If INPUT_STRING matches bye then the goodbye message is printed and the loop exits. Note that if we wanted to exit the script 
# completely then we would use the command exit instead of break.
# The third option here, the *), is the default catch-all condition; it is not required, but is often useful for 
# debugging purposes even if we think we know what values the test variable will have.

# The whole case statement is ended with esac (case backwards!) then we end the while loop with a done.

# That's about as complicated as case conditions get, but they can be a very useful and powerful tool. 
# They are often used to parse the parameters passed to a shell script, amongst other uses.

# we have to help this rude robot and cure his loneliness! Create a robot - Start off with robot asking for your name and have 
# you input your name in. When after name has been inputted, ask a statement to user about wanting to chat. Have user input a string(s) to have 
# a reply back. For example. Robot: "How is your day?"  User: "Good!" Robot:
#"I don't care about your day <user name>! I am leaving!" and ends the program.
#Example 2. Robot: "Talk to me!" User: "lets play a game" Robot: "You didn't program me to play a game!" "What do you
# want to do now?" User: "bye" Robot: "Bye <user name>!" and ends the program. 
#Think about it and we will go over it in class. HINT: If there is a IF and ELSE statement, there is CASE statement! 
#!/bin/bash

# echo "Hello I want to be your friend"
# echo "What is your name"
# read MyName #MyName is a variable that holds user input
# echo "please tell me why your here"
# while :
# do
#     read INPUT_STRING
#     case $INPUT_STRING in 
#         hello)
#             echo "hello $MyName"
#             echo " whats up"
#             ;;
#         "good morning")
#             echo "good evening"
#             break
#             ;;
#         *)
#             echo "sorry I dont understand"
#             ;;
#     esac
#done

echo "Hello what doctor are you here to see"
read MyDoctor
echo  "Ok let me get you checked in, whats your birthdate"
read MyDateOfBirth #MyDateOfBirth is a variable that holds user input
echo "Oh your birthdate is right around the corner, and what is your height"


while :
do
    read INPUT_STRING
    case $INPUT_STRING in
        "5'11")
    
            echo "hello $MyDoctor"
            echo "Lets get you squared away"
            echo " what is your weight?"
            ;;
        "175lb")
            echo "ok have a seat will get you going"
            break
            ;;
        160lb)
            echo "looking good lets reschedule"
            break
            ;; 


        "you are looking awesome")
            echo "you are looking marvalous as well"

            break
            ;;
        *)
            echo "so tell me more of what brings you in today besides your bloodpressure"
    
            ;;
            
    esac
done

