#!/usr/bin/env python
# encoding: utf-8

import os
import netaddr


def main():

    count = 0

    for ip_CIDR in open('china_ip_list.txt', 'r'):
        # cidr = int(ip_CIDR.split('/')[1])
        # if cidr < 24:
        #     continue
        ips = netaddr.IPNetwork(ip_CIDR.strip())
        count += len(ips)
        # for ip in ips:
            # self.in_queue.put('http://' + str(ip).strip() + ':8161')
    print count


if __name__ == '__main__':
    os.system('clear')

    main()
