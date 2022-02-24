#!/bin/bash

# Ops Challenge: File Permissions
# Overview
# Linux sets file permissions by User, Group, and Other. Linux also sorts permission by Read, Write, and Execute. Today, you will be create a bash script that alters file permissions of everything in a directory.

# Objectives
# Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

# Create a new bash script that performs the following:

# Prompts user for input directory path.
# Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
# Navigates to the directory input by the user and changes all files inside it to the input setting.
# Prints to the screen the directory contents and the new permissions settings of everything in the directory.

echo -n "Enter Source Directory:"
read srcdir
echo -n "Enter Destination Directory:"
read dstdir
rsync -av --delete "$srcdir" "$dstdir"

ls -l filename.txt
chmod g=r filename

dirs=(*/)

read -p "$(
        f=0
        for dirname in "${dirs[@]}" ; do
                echo "$((++f)): $dirname"
        done

        echo -ne 'Please select a directory > '
)" selection

selected_dir="${dirs[$((selection-1))]}"

echo "You selected '$selected_dir'"