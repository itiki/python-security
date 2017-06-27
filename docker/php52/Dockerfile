FROM debian:6

MAINTAINER xinali daitaomail@gmail.com

# php5 from squeeze => 5.2
RUN echo "deb http://archive.debian.org/debian lenny main contrib non-free" > /etc/apt/sources.list.d/php.list
RUN echo "Package: php5 php-apc php-http php-http-request php-net-socket php-net-url php-pear php5-cli php5-common php5-curl php5-dev php5-gd php5-ldap php5-mcrypt php5-mysql php5-xsl" > /etc/apt/preferences.d/lenny
RUN echo "Pin: release n=lenny*" >> /etc/apt/preferences.d/lenny
RUN echo "Pin-Priority: 999" >> /etc/apt/preferences.d/lenny
RUN apt-get update
RUN apt-get install -y php-apc php-http php-http-request php-net-socket php-net-url php-pear php5-cli php5-common php5-curl php5-dev php5-gd php5-ldap php5-mcrypt php5-mysql php5-xsl

# Install PHP HttpRequest
RUN apt-get install -y libcurl4-openssl-dev make
RUN ln -s /usr/share/libtool/config/ltmain.sh /usr/share/libtool/ltmain.sh
RUN ln -s /usr/share/aclocal/libtool.m4 /usr/share/libtool/libtool.m4
RUN cd /usr/share/aclocal/ && cat lt~obsolete.m4 ltoptions.m4 ltsugar.m4 ltversion.m4 >> libtool.m4
#RUN echo "\n"|pecl install pecl_http-1.7.6
RUN echo "\n"|pecl install pecl_http-1.6.3
RUN echo "extension=http.so" > /etc/php5/conf.d/20-http.ini

# Install PHP OLE for obsExcel
RUN pear install channel://pear.php.net/OLE-1.0.0RC2
