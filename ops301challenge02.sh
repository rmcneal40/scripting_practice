

#Create a bash script that:
# Copies /var/log/syslog to the current working directory
# Appends the current date and time to the filename
# For shell scripts, format your code according to the shell style guide linked above.


#!/bin/sh
if ! [ $1 ] ; then
        echo "Usage:";
        echo $0 "<directory_where_to_save_logs>";
        return;
fi

if [ ! -d "$1" ]; then
  echo "Creating directory $1";
  mkdir $1;
fi

cp /var/log/syslog* $1
cp /var/log/dmesg* $1