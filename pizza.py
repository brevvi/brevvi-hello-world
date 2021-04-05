#! /usr/bin/env python

# pizza cardapio

toppings = ['mushroom', 'peperoni', 'cheese']
mytoppings = []


def escolha():
    choose = str(input('Do you like mushrooms in your pizza? [Yes | No]'))
    choice = choose.title()
    if (choice == 'Yes' or choice == 'Y'):
        mytoppings.append(toppings[0])
    choose = str(input('Do you like peperoni in your pizza? [Yes | No]'))
    choice = choose.title()
    if (choice == 'Yes' or choice == 'Y'):
        mytoppings.append(toppings[1])
    choose = str(input('Do you linke chesse in your pizza? [Yes | No]'))
    choice = choose.title()
    if (choice == 'Yes' or choice == 'Y'):
        mytoppings.append(toppings[2])
    print('You choose a pizza with this toppings: ' + str(mytoppings))

print("Choose your pizza's topping")
escolha()
