#!/bin/sh

# Wordpress Randomiser
/usr/bin/python3.8 /root/wordpress_random.py

rm -rf rm /var/www/localhost/htdocs/index.html

# This is a lazy way to start it find a better way. 
httpd

exec "$@"