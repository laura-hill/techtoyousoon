#! /bin/bash
yum update -y
yum install python3 -y
pip3 install flask
pip3 install flask_mysql
yum install git -y
TOKEN="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"
cd /home/ec2-user && git clone https://$TOKEN@github.com/laura-hill/phonebook.git
python3 /home/ec2-user/phonebook/phonebook-app.py