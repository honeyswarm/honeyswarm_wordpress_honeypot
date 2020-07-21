FROM alpine:latest

RUN apk add --repository=http://dl-cdn.alpinelinux.org/alpine/edge/community --no-cache python3 py3-pip py3-gunicorn py3-aiohttp openssl apache2 php7-apache2 php7-sqlite3 php7-pdo_sqlite php7-pdo_mysql php7-json
RUN pip install --no-cache-dir hpfeeds

ADD filesystem /
RUN chmod +x /docker-entrypoint.sh

ADD htdocs.tar.gz /var/www/localhost

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/bin/python3.8", "/root/prox.py"]