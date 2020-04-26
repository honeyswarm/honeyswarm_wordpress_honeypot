# Now build the Wordpress container Install the plugins and copy over the report
FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

ENV CUSTOM_APPS="mysql-server apache2 php libapache2-mod-php php-mysql nano python3.8 python3-pip locales"
RUN apt-get update && apt-get install --reinstall -yqq \
      $CUSTOM_APPS \
    && apt-get -y clean \
    && apt-get -y autoremove

RUN rm /var/log/apache2/error.log /var/log/apache2/access.log
RUN usermod -d /var/lib/mysql/ mysql
RUN locale-gen en_US.UTF-8

# Python Libs
RUN python3.8 -m pip install requests faker hpfeeds mitmproxy requests aiohttp

# Add the base install
ADD --chown=www-data:www-data html.tar.xz /var/www/
RUN chown -R www-data:www-data /var/www/html
RUN rm /var/www/html/index.html

# Add all our customisation and startup scripts
ADD root /root
ADD 000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ports.conf /etc/apache2/ports.conf

# Set the startup script
CMD ["/bin/bash", "/root/startup.sh"]
