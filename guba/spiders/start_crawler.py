#!/usr/bin/env python
# encoding: utf-8

import os
import re

def get_file_name(pre_name, count):
    if len(count) == 1:
        return pre_name + '_' + '0' + count + '.txt'
    else:
        return pre_name + '_' + count + '.txt'

def modify_files():
    directory = 'stocknum_03'
    file_nums = 10
    count = 1
    for name in xrange(file_nums):
        file_name = get_file_name(directory, str(count))
        file_name = directory + '\\' + file_name
        count += 1
        old_file = open('spider.py', 'r')
        codes = old_file.readlines()
        codes_len = len(codes)
        pattern = re.compile(r'stocknum_(\d+)\\stocknum_(\d+)_(\d+).txt')
        j = 0
        for code in codes:
            find = pattern.search(code)
            result = pattern.sub(file_name, code)
            if result and find:
                codes[j] = result
                # print '\n###########################################################\n'
                print 'find and replace, so handle', file_name, '........\n'
            j += 1
        new_file = open('spider.py', 'w')
        for line in codes:
            new_file.write(line)
        new_file.close()
        # raw_input('handle file successfully....')

if __name__ == '__main__':
    os.system('printf "\033c"')
    os.system('color 02')

    modify_files()
