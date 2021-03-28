#! /usr/bin/env python
"""
    select a people from a list to have a dinner with
"""
import time

places = dict([[1,'Sushiland'],[2,'GoVegans'],[3,'TexMexRanch'],[4,'VeryFancyPlace']])
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
            newname = str(input('Do you like to suggest a new name:' + '\nNew name: '))
            grlck.insert(numb, newname)
        numb = numb + 1
    girls = grlck.copy()
    return girls

def places4dinner():
    global places
    places = dict([[1,'Sushiland'],[2,'GoVegans'],[3,'TexMexRanch'],[4,'VeryFancyPlace']])

def invite():
    numb = 0
    for i in range(len(girls)):
        girl = girls.pop(numb)
        print('Hi,','{}'.format(girl),'!','\nDo you like to have a dinner with me?')
        answer = str(input('Yes or No?'))
        answer = answer.title()
        if (answer == 'Yes' or answer == 'Y'):
            print("Great! Do you like to chosse the place for dinner")
            print(places)
            theplace = int(input('Chosse one of the numbers of the list, please: '))
            print('Great! I meet you in the '+places[theplace]+'at 7pm. XOXO!')
            time.sleep(1)
            break
        else:
            print("Oh... It's Okay then... Bye")
            time.sleep(1)
    return

checklist()
invite()
