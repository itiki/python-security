#encoding:utf-8

import os
import dns.resolver
from thread_template import runThreads
from queue import Queue

in_queue = Queue()

def init_date():

    for site in open('top_sites.txt', 'r'):
        in_queue.put(site.strip())


def handle():

    while in_queue.qsize() > 0:
        site = in_queue.get()
        try:
            ans = dns.resolver.query(site, 'ns')
            if ans:
                ns = ans[0]
                bind_version = os.popen('dig chaos txt version.bind @%s +short' % ns)
                print ("-"*100)
                i = 0
                for v in bind_version:
                    if '"' in v:
                        print (site, v.strip())
                    break
        except Exception as ex:
            print (ex)


if __name__ == '__main__':
    os.system('clear')
    init_date()
    runThreads(20, handle)
