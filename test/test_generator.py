#!/usr/bin/env python
# encoding: utf-8

def fib():
    a = b = 1
    yield a
    yield b

    while True:
        yield a+b
        a, b = b, a+b


if __name__ == '__main__':

    fb = fib()

    
    for num in fb:
        if num > 100:
            break
        print num
