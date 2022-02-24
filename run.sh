#!/bin/bash 
echo `cat students.txt | awk '{print $2}'`