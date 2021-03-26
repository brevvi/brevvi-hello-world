#! /usr/bin/env python
import sys
import time

hello = 'Hello. What is your name?'
name = ''

def yourname(name):
    time.sleep(1)
    name = input('Type your name here:')
    time.sleep(1)
    print('Hello','{}.'.format(name), 'How are you?')
    return

print(hello)
yourname(name)

