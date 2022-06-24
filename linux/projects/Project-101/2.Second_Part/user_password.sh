#!/bin/bash
if [ $(id -u) -ne 0 ]
then 
    echo "you must be root to run this script"
    exit 0
fi
read -p "enter the username: " uname
read -p "type the full name enclosed in double quotes: " comment
read -p "enter the password: " pw 
useradd -c "$comment" $uname
if [ $? -eq 0 ]
then
    echo "account succesfully created"
else
    echo "account creation failed"
    exit 1
fi
echo -e "${pw}\n${pw}\n" | passwd $uname
if [ $? -eq 0 ]
then
    echo "password succesfully created"
else
    echo "password creation failed"
    exit 2
fi
chage -d 0 $uname
echo "$uname, $pw, $(hostname)"