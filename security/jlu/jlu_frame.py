#encoding:utf-8
import os
import netaddr
import requests

import urllib2
import sys
from poster.encode import multipart_encode
from poster.streaminghttp import register_openers


def exploits():
    ips = netaddr.IPRange('202.198.16.0', '202.198.31.255')
    for ip in ips:
        print ip
        raw_input('wait...')


def main():
    poc()


if __name__ == '__main__':
    main()
