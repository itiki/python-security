#encoding: utf-8

import os
import commands
import time

def start_php52():
    print commands.getoutput('docker ps -a -q | xargs docker rm -f 2>/dev/null')
    sufix = commands.getoutput('date +%s')

    # print commands.getoutput('docker run --name mysql' + sufix + ' -d -v /var/lib/mysql:/var/lib/mysql xinali/mysql55 /usr/sbin/mysqld')
    # print commands.getoutput('docker run --name mysql' + sufix + ' -d xinali/mysql55 /usr/sbin/mysqld')
    # print commands.getoutput('docker run --name mysql' + sufix + ' -v /var/lib/mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=daitao -d test/mysql')
    print commands.getoutput('docker run --name mysql' + sufix + ' -e MYSQL_ROOT_PASSWORD=daitao -d xinali/mysql')
    print commands.getoutput('docker run --name apache -p 80:80 --link mysql' + sufix + ':mysql -v /owaspbwa:/var/www xinali/apache22-php52 apache2ctl -D FOREGROUND')


if __name__ == '__main__':
    os.system('printf "\033c"')

    start_php52()
