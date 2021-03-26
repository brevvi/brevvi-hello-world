#! /usr/bin/env python
import sys
import time

hello = 'Hello. What is your name?'
name = ''

def yourname(name):
    time.sleep(1)
    name = input('Type your name here:\t')
    time.sleep(1)
    name = name.title()
    name = name.lstrip()
    name = name.rstrip()
    print('Hello','{}.'.format(name), '\nHow Zen are you?')
    return

print(hello)
yourname(name)

import this
