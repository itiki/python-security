FROM php:5.6-apache

# Install php extensions
RUN echo "deb http://mirrors.163.com/debian/ jessie main non-free contrib" > /etc/apt/sources.list \  
    && echo "deb http://mirrors.163.com/debian/ jessie-updates main non-free contrib" >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y libpng12-dev libjpeg-dev wget mysql-server\
    && docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \
    && docker-php-ext-install -j$(nproc) mysqli gd zip


# Download and Extract SugarCRM
RUN wget https://codeload.github.com/sugarcrm/sugarcrm_dev/tar.gz/6.5.23 -O src.tar.gz \  
    && tar -zxvf src.tar.gz \
    && mv sugarcrm_dev-6.5.23/* /var/www/html \
    && rm src.tar.gz
