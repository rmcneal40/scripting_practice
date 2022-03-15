import argparse
import sys

try:
     parser = argparse.ArgumentParser()
     parser.add_argument("square", help="display a square of a given number",
                type=int)
    args = parser.parse_args()

    #print the square of user input from cmd line.
    print args.square**2

    #print all the sys argument passed from cmd line including the program name.
    print sys.argv

    #print the second argument passed from cmd line; Note it starts from ZERO
    print sys.argv[1]
except:
#     e = sys.exc_info()[0]
#     print e

#     rompt the user to select a HTTP Method of the following options:
# GET
# POST
# PUT
# DELETE
# HEAD
# PATCH
OPTIONS