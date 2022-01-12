#!/bin/bash

c=1

while [ $c -le 5 ]
do
	echo "Welcone $c times"
	(( c++ ))
done


# set yname="foo"
# while ( $yname != "" )
# 	echo -n "Enter your name : "
# 	set yname = $<
# 	if ( $yname != "" ) then
# 		echo "Hi, $yname"
# 	endif
# end
