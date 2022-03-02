#!/bin/bash
# Write a bash script that clears the contents of these logs:

# /var/log/syslog
# /var/log/wtmp
# Print to screen the before and after of the contents of each file.

# Add the below information as comments:

# Script Name
# Author
# Date of last revision
# Description of purpose
# Declaration of variables
# Declaration of functions
# Main
# End

# cd /var/log/nginx/
#  ls -lh www.cyberciti.biz_access.log
# truncate -s 0 www.cyberciti.biz_access.log
#  ls -lh www.cyberciti.biz_access.log

 script= logs() {
     echo "Date of Last revision"
     echo "Description of purpose"
     echo "Declaration of funtions"
     Main
     End
 }
 logs
