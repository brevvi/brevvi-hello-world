#! /usr/bin/env python
"""
    select a people from a list to have a dinner with
"""
import time

girls = ['Jessica Alba','Alexandra Daddario', 'Mary Elizabeth Winstead']
numb = 0

def invite():
    #print(girls)
    for i in range(len(girls)):
        #print(girls)
        girl    =  girls.pop(numb)
        print('Hi,'+girl+'!''\nDo you like to have a dinner with me?')
        answer = str(input('Yes or No?'))
        answer = answer.title()
        #print(answer)
        if (answer == 'Yes' or answer == 'Y'):
            print("Great! I'll get you at 7pm! XOXO!")
            time.sleep(1)
            break
        else:
            print("Oh... It's Okay then... Bye")
            time.sleep(1)
    return

invite()
