'''
zombie surivial game:

health:100
food:5
ammo:5
Money:100


What do you want to do?

1. 🏠 Search a building
2. 🧟 Fight zombies
3. 🍗 Eat food
4. 🛒 Visit shop
5. 💤 Sleep
6. 🚪 Quit

DAY :1

when player search building:

random things:
food:2,ammo:10,Money:2

another zombie found you
random health reduce:


2)fight zombie:

display zombie health:
oppent zombie heath:

shoot or run:


3)eat food:
food -1
health +20

4)shop:

food:
ammo:
medicin:

5)sleep:

day 2 satrt

'''

import random


zombieData = {'health': 100, 'food': 5, 'ammo': 50, 'money': 100}
dataList = ['health', 'food', 'ammo', 'money']
shopItems = {'food': 67, 'ammo': 100, 'medicin': 150}

day = 1
searchBul = 0


def searchBuilding():
    global searchBul

    searchBul += 1
    zombieFound = False

    if searchBul == 3:
        searchBul = 0
        zombieFound = True

    foundList = random.choices(dataList, k=random.randint(1, len(dataList)))

    if len(foundList) == 0:
        print('Found Nothing in this Building...')
    elif zombieFound:
        fightZombies()
    else:
        for i in foundList:
            amount = random.randint(0, 6)
            print(f'{amount} {i} Found...')
            if zombieData[i] != 'health':
                zombieData[i] += amount
            else:
                continue

    return


def fightZombies():

    secondZombieHealth = random.randint(1, 101)

    print('Other Zombiee Spoted You...')
    print('You have to Option')
    print('1. Fightttt')
    print('2. Runnnn')
    fzChoice = int(input('What would you like to do? : '))

    match fzChoice:

        case 1:
            print('----- WAPONS -----')
            print('1. Amom')
            print('2. Boxing')
            wChoice = int(input('Which Wapon would you like to use : '))

            match wChoice:

                case 1:
                    while secondZombieHealth > 0:
                        print(f'Your Health : {zombieData["health"]}')
                        print(f'Zombiee Health : {secondZombieHealth}')
                        print('Firing....')
                        secondZombieHealth -= 20
                        print('Zombiee Health -20...')
                        zombieData["health"] -= random.randint(1, 8)
                        if zombieData['health'] == 0:
                            print('You Died Fighting Other Zombiee...')

                    print('Eureka!!You Defeted the Zombiee in the Fight...')
                    return

                case 2:

                    while secondZombieHealth > 0:
                        print(f'Your Health : {zombieData["health"]}')
                        print(f'Zombiee Health : {secondZombieHealth}')
                        print('Punching....')
                        secondZombieHealth -= 10
                        print('Zombiee Health -20...')
                        zombieData["health"] -= random.randint(1, 8)
                        if zombieData['health'] == 0:
                            print('You Died Fighting Other Zombiee...')

                    print('Eureka!!You Defeted the Zombiee in the Fight...')
                    return

        case 2:
            hamout = random.randint(1, 3)
            print('Running at 67km/hr....')
            zombieData['health'] -= hamout
            return


def eatFood():

    if zombieData['health'] >= 100:
        print('You Can\'t Eat more Food...\n\tYour Health is Full...')
    else:
        zombieData['food'] -= 1
        zombieData['health'] += 5
        print('Health Increased +5...')
        if zombieData['food'] <= 0:
            print('You have no food...\n\tPlease visti shop or a buliding...')

    return


def sleep():

    global day

    print('---SWEET DREAMS---')
    day += 1
    return


def visitShop():

    for i in shopItems:
        print(f'Item : {i} | Price : {shopItems[i]}')

    item = input('Enter the Item you want : ')
    qty = int(input('Enter the Quantity of the Item : '))

    bill = shopItems[item] * qty
    if zombieData['money'] <= 0 and zombieData['money'] < bill:
        print('You Don\'t have enough Money...')
    else:
        zombieData['money'] -= bill
        if item == 'medicin':
            zombieData['health'] += 20
            print(f'Health Increased +{20 * qty}...')

        print(f'Your total bill : {bill}')
        print('Thank You..\n\tDo Visit Again...')

    return


print('---------- WELCOME TO ZOMBIE SURVIVAL GAME ----------\n\n')

while True:

    print(f'========= DAY : {day} =========\n')
    print('--------- OPTIONS ---------')
    print('1. Search a building')
    print('2. Fight zombies')
    print('3. Eat food')
    print('4. Visit shop')
    print('5. Sleep')
    print('6. Quit')
    choice = int(input('What Would you like to do next? : '))

    match choice:

        case 1:
            searchBuilding()
        case 2:
            fightZombies()
        case 3:
            eatFood()
        case 4:
            visitShop()
        case  5:
            sleep()
        case 6:
            print('Exitig the game...')
            break
        case _:
            print('Please Enter a valid choice...')
