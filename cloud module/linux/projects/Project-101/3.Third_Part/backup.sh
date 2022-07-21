#!/bin/bash
if [ $(id -u) -ne 0 ]
then
   echo "you must be root to run this script"
   exit 0
fi
tar czf /mnt/backup/$(hostname)-$(date +%F-%H-%M).tgz /home/ec2-user/data /etc /boot /usr