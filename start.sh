#! /bin/bash

sudo dnf update -y
sudo dnf install php php-cli php-common php-fpm php-mysqlnd -y
sudo dnf install httpd -y
sudo dnf install git-all -y
sudo systemctl start httpd
git clone git@github.com:DeboraSerra/Assignment5-IST105.git
sudo cp -r Assignment5-IST105/* /var/www/html/
sudo systemctl restart httpd
