#! /usr/bin/env python
"""
    select a people from a list to have a dinner with
"""
import time

#girls = ['Jessica Alba','Alexandra Daddario', 'Mary Elizabeth Winstead']
numb = 0

def checklist():
    global  girls
    girls = ['Jessica Alba','Alexandra Daddario', 'Mary Elizabeth Winstead']
    grlck = girls
    newname = ' '
    numb = 0
    for i in range(len(grlck)):
        grlcklst = grlck.pop(i)
        print(grlcklst)
        time.sleep(1)
        print(grlcklst+':'+'RSVP')
        ckconf = str(input(grlcklst+' : '+'Confirm presence? '+'Yes or No? '))
        ckconf = ckconf.title()
        if (ckconf == 'Yes' or ckconf == 'Y'):
            print('Presence  confirmed!')
            grlck.insert(numb, grlcklst)
        else:
            newname = str(input('You do like to suggest a new name:' + '\nNew name: '))
            grlck.insert(numb, newname)
        numb = numb + 1
    girls = grlck.copy()
    return girls

def invite():
    numb = 0
    for i in range(len(girls)):
        girl = girls.pop(numb)
        print('Hi,'+girl+'!''\nDo you like to have a dinner with me?')
        answer = str(input('Yes or No?'))
        answer = answer.title()
        if (answer == 'Yes' or answer == 'Y'):
            print("Great! I'll get you at 7pm! XOXO!")
            time.sleep(1)
            break
        else:
            print("Oh... It's Okay then... Bye")
            time.sleep(1)
    return

checklist()
invite()
