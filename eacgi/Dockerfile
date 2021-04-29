FROM debian
LABEL maintainer="carefuldata@protonmail.com"
LABEL version="1.1"
LABEL description="EaaS API condensed service template"

RUN apt-get update && apt-get install -y apt-transport-https aptitude && aptitude install -y openssl apache2 xxd gnupg2 netcat haproxy
COPY apache2.conf /etc/apache2/apache2.conf
COPY serve-cgi-bin.conf /etc/apache2/conf-enabled/
COPY zcrab.cgi /var/www/html/
COPY haproxy.cfg /etc/haproxy/haproxy.cfg
COPY keycert.pem /etc/keycert.pem
COPY ZCRAB /usr/local/sbin/
RUN ln -sf /dev/stdout /var/log/cgi.log
RUN ln -sf /dev/null /var/log/apache2/access.log
RUN a2enmod cgi

EXPOSE 80
EXPOSE 9642

CMD gpg --list-keys --homedir=/root/
CMD ZCRAB
