#!/bin/bash

# we may need a commit to get all the data in to the db
chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
service mysql start
service apache2 start

# Randomise the SQL file
cd /root && python3.8 /root/wordpress_random.py

# import the SQL file
mysqladmin -u root password 'sqlpassword'
mysql -u root -p'sqlpassword' < /root/database.sql
mysql -u root -p'sqlpassword' -Bse "GRANT ALL PRIVILEGES ON *.* TO 'wordpressuser'@'%' IDENTIFIED BY 'wordpresspassword';"
# Restart the apache server

# Run the Plugin Installer
sleep 5
cd /root && python3.8 /root/plugin_installer.py
# Add any SQL files

# Run the Proxy and reporting
cd /root && python3.8 /root/prox.py