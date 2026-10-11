'''
1. 🏝️ Island Survival Challenge
Beginner → Intermediate
Story: Your plane crashes on a mysterious island. Survive for 10 days until rescue arrives.
Starting stats: Health 100, food 3, water 3, wood 0.
Tasks
- Search the island for food and water.
- Collect wood to build a shelter.
- Hunt animals for food.
- Random storms can damage your shelter.
- Every day consumes food and water.
Boss challenge: Survive a massive storm on Day 10.
--------------------------------------------------------------------------------------------------------------------------------

Desinging : 

stats = {'Health' : 100, 'Food' : 3, 'Water' : 3, 'Wood' : 0}
hugurCounter = 100 #in percent
thrustCounter = 100 #in percent
dayCounter = 1

first tell the story 

when sleep check --> is there a shelter ? yes -> sleep no -> prompt that you must build shelter first

when drink water  : 
    check -> is trustCounter : 100% ? yes -> prompt can't drink more water
                                      no -> increase the thrustCounter by 5 and decr the water in stats by 1 

when eating food  : 
    check -> is hungerCounter : 100% ? yes -> prompt can't eat food
                                      no -> increase the hungerCounter by 5, health by 7 and decr the food in stats

when buildingShelter : 
    check if hitStorm : you can't build shelter in Storm
    else : 
        check -> do player have enough Wood :
                yes -> prompt building shelter and decrease wood accordingly 
                       also 
                       if thrustCount <= 0 : you died thriving for water and return 
                       else if thrustCount <= 35 : you have to drink water for survival
                       else :  deacrese thrustCount by 20
                       if hungerCount <= 0 : you died starving for food and return 
                       else if hungerCount <= 35 : you have to eat food for health and survival
                       else :  deacrese hungerCount by 25
                no -> prompt not have enough wood to build 

when hunting animal : 
check : 
        generate random animal health : 
        while(animal is not 0) : 
            fight and randomly deacrease the animal's
            and player's health 
            in betwenn also check the player's health
            and also randomly deacrease the 
            player's hungerCount and thrustCount
        return

when collocting wood : 
check hasStorm || day 10 : 
    print('You Can\'t Go For Hunting in the Strom....')
            if not checkHealth:
                stats['Health'] -= random.randint(1, 31)
                checkHealth()
                hugurCounter -= random.randint(1, 26)
                checkThrust()
                thrustCounter -= random.randint(1, 21)
            elif checkHealth == -1:
                print('Warning! You Have Low Health...')
            else:
                print('You Died Challenging...')
                print('Well Played Player!!')
                return


when search island  :
check is strom  :
 print you can't go outside 
 else :
    randomly generate the item no and amount and add it 
    and also gradually decre the health, hungerCounter and thrustCounter
        

'''

import random
import time

stats = {'Health': 88, 'Food': 3, 'Water': 3, 'Wood': 0}
itemsCouldBeFound = ['Food', 'Wood', 'Water']
hugurCounter = 50  # in percent
thrustCounter = 67  # in percent
dayCounter = 1
haveShelter = False
isAlive = True


def clear_screen():
    print("\033[H\033[J", end="")

# sorty itmeee


def beforStory():

    print('=================================== BEFORE STORY ===================================')
    time.sleep(1)
    print('You (THINKING) : Ah! What a great day.\n\tFinaly going back home after a long Time..')
    time.sleep(3.5)
    print('You (THINKING) : I will give suprice to my family \n\tand we will celebrate the New Year Together....')
    time.sleep(3.5)
    print('Wait What..!! What is happenning...')
    time.sleep(3.5)
    print('The Radar started Flactuating...')
    time.sleep(3.5)
    print('The engine blew up, sending the plane diving fast toward a strange jungle island.')
    time.sleep(2.5)
    print('The plane tore open, and everyone put on oxygen masks as bags flew everywhere.')
    clear_screen()
    time.sleep(2)
    print('BHOMMM..')
    time.sleep(2)
    print('The Plane Crashed!!!')
    time.sleep(3.5)


def afterCrash():

    clear_screen()
    print('=================================== AFTER CRASH ===================================')
    time.sleep(2)
    print('You woke up alone on a dark beach next to the broken pieces of the plane.')
    time.sleep(3.5)
    print('You (THINKING) : What happened and how it happened...')
    time.sleep(3.5)
    print('You Saw Your Watch..\n\tGlass Broken Stated 17th dec.')
    time.sleep(3.5)
    print('You Realised that a Patroling helecotor will Come for patroling after 10 days...')
    time.sleep(3.5)
    print('So Now You have to Survive in this Island For 10 days....')
    time.sleep(1.5)
    clear_screen()

def finalDay() : 

    clear_screen()
    print('The scary Day 10 storm finally stops, \n\tand the warm morning sun shines down on the battered beach.')
    time.sleep(2.5)
    print('You hear a beautiful sound in the sky—the loud, \n\tthumping rotors of a rescue helicopter coming to save you.')
    time.sleep(2.5)
    print('Your heart fills with joy as you step out of your shelter, \n\tknowing you safely made it through ten long, lonely days.')
    time.sleep(2.5)
    print('The kind rescue crew pulls you inside, \n\twrapping you in a warm blanket as you finally let out a deep sigh of relief.')
    time.sleep(2.5)
    print('You look out the window at the mysterious island fading away, \n\tproud that you fought hard and won the ultimate survival game!')
    time.sleep(1.5)
    print("============= YOU WON =============") 
    return 

def hitStorm():

    storm_chance = random.randint(1, 101)

    if storm_chance <= 20:
        return True
    else:
        return False

actionsToday = 0
ACTIONS_PER_DAY = 3

def endAction():
    global isAlive, actionsToday
    actionsToday += 1                  
    healthManager()
    if stats['Health'] <= 0:
        stats['Health'] = 0
        isAlive = False
        print('You Died Challenging...\nWell Played Player!!')
    elif hugurCounter <= 35 or thrustCounter <= 35:
        print('Warning! You are weak from hunger or thirst...')


def sleep():
    global dayCounter, actionsToday

    if not haveShelter:
        print('To Sleep Securely You have to build a Shelter!!')
        return

    if actionsToday < ACTIONS_PER_DAY:
        print(f'You are not tired yet. Do {ACTIONS_PER_DAY - actionsToday} more action(s) first.')
        return

    print('---SWEET DREAMS---')
    dayCounter += 1
    actionsToday = 0

def healthManager():

    global thrustCounter, hugurCounter

    if thrustCounter > 0:
        thrustCounter -= random.randint(1, 8)
    else:
        thrustCounter = 0
        stats['Health'] -= random.randint(1, 11)

    if hugurCounter > 0:
        hugurCounter -= random.randint(1, 8)
    else:
        hugurCounter = 0
        stats['Health'] -= random.randint(1, 11)

    return


def searchIsland():

    global hugurCounter, thrustCounter

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Searching Island in the Strom....')
        stats['Health'] -= random.randint(5, 15)
        print('The storm batters you!')
        endAction()
        return
    else:
        print('Searching Island....')
        time.sleep(3)
        endAction()
        foundList = random.choices(
            itemsCouldBeFound, k=random.randint(1, len(itemsCouldBeFound)))
        if len(foundList) == 0:
            print('Found Nothing in this Building...')
            return
        else:
            for i in foundList:
                amount = random.randint(0, 6)
                stats[i] += amount
                print(f'{amount} {i} Found...')
            return


def collectWood():

    global hugurCounter, thrustCounter

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Collecting Wood in the Strom....')
        stats['Health'] -= random.randint(5, 15)
        print('The storm batters you!')
        endAction()
        return
    else:
        print('Collecting Woods...')
        time.sleep(3)
        woodAmout = random.randint(1, 21)
        endAction()
        stats['Wood'] += woodAmout
        print(f'You Collected {woodAmout} Woods....')
        return


def huntAnimals():

    global hugurCounter, thrustCounter

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Hunting in the Strom....')
        stats['Health'] -= random.randint(5, 15)
        print('The storm batters you!')
        endAction()
        return
    else:
        clear_screen()
        print('SEARCHING......')
        time.sleep(3)
        print('Animal Found...')

        animalHealth = random.randint(35, 101)

        while animalHealth > 0:

            print('Attackking....')
            animalHealth -= random.randint(1, 21)
            stats['Health'] -= random.randint(1, 5)
            print('The animal hits back!')
            endAction()
            if not isAlive:
                return

        foodAmount = random.randint(1, 11)
        stats['Food'] += foodAmount
        print(
            f'Eureka You Killed the Animal.. \n\t You got {foodAmount} Amount of Food')

        return


def checkHealth():

    global isAlive

    if stats['Health'] <= 0:
        stats['Health'] = 0
        isAlive = False
        return True
    elif hugurCounter <= 35:
        return -1
    return False


def buildShelter():

    global thrustCounter, hugurCounter, haveShelter
    aFrameShelterWood = 10
    leanToShelterWood = 20
    logCabinShelterWood = 35

    if hitStorm():
        print('You can not build Shelter in Storm...')
        stats['Health'] -= random.randint(5, 15)
        print('The storm batters you!')
        endAction()
        return
    else:
        print('1. A-Frame Tarp Shelter (Small).')
        print('2. Lean-To Brush Hut (Medium)')
        print('3. Log Cabin Box (Large)')
        shChoice = int(input('What Type of Shelter You Want to Build : '))

        match shChoice:

            case 1:
                if stats["Wood"] <= aFrameShelterWood:
                    print('You Don\'t have enough Wood to Build this shelter....')
                    return
                else:
                    print('Building A-Frame Tarp Shelter...')
                    haveShelter = True
                    stats['Wood'] -= aFrameShelterWood
                    endAction()
                    return

            case 2:
                if stats["Wood"] <= leanToShelterWood:
                    print('You Don\'t have enough Wood to Build this shelter....')
                    return
                else:
                    print('Building Lean-To Brush Hut Shelter...')
                    stats['Wood'] -= leanToShelterWood
                    haveShelter = True
                    endAction()
                    return

            case 3:
                if stats["Wood"] <= logCabinShelterWood:
                    print('You Don\'t have enough Wood to Build this shelter....')
                    return
                else:
                    print('Building Log Cabin Box Shelter...')
                    stats['Wood'] -= logCabinShelterWood
                    haveShelter = True
                    endAction()
                    return

            case _:
                print('Please Enter a valid Choice')


def eatFood():

    global hugurCounter

    if stats['Food'] <= 0:
        print('You Don\'t have Enough Food to Eat...')
        print('Please Search Island or Hunt For More Food...')
        return
    else:
        if hugurCounter >= 100:
            hugurCounter = 100
            print('Yon Can Not Drink More Water...')
            return
        else:
            print('Eating Food....')
            hugurCounter = min(100, hugurCounter + 5)
            stats['Health'] += 7
            if stats['Health'] >= 100:
                stats['Health'] = 100
                print('Your Health is Full...')
            else:
                print('Health Increased By +7....')
            if hugurCounter >= 100 and stats['Health'] >= 100:
                print('You Are Full and Healthy...')
                return
            stats['Food'] -= 1

        return


def drinkWater():

    global thrustCounter

    if stats['Water'] <= 0:
        print('You Don\'t have Enough Water to Drink...')
        print('Please Search Island For More Water...')
        return
    else:
        if thrustCounter >= 100:
            thrustCounter = 100
            print('Yon Can Not Drink More Water...')
            return
        else:
            print('Drinking Water....')
            thrustCounter += 5
            stats['Water'] -= 1

        return


# beforStory()
# afterCrash()

print('---------- WELCOME TO ISLAND SURVIVAL CHALLENGE ----------\n\n')



while isAlive:

    if dayCounter == 10:
        print('------------------------------ FINAL DAY ------------------------------')
    elif isAlive and dayCounter == 11:
        finalDay()
        break

    print(f'========= DAY : {dayCounter} =========\n')

    print(f'Your Details : {stats}')
    print(f'Hunger Percent : {hugurCounter}%')
    print(f'Thrust Percent : {thrustCounter}%\n')

    print('--------------------- OPTIONS ---------------------')
    print('1. Search the island for food and water.')
    print('2. Collect wood to build a shelter.')
    print('3. Hunt animals for food.')
    print('4. Build The Shelter.')
    print('5. Eat Food.')
    print('6. Drink Water.')
    print('7. Sleep.')
    print('8. Quit')
    choice = int(input('What Would you like to do next? : '))

    match choice:

        case 1:
            searchIsland()
            pass
        case 2:
            collectWood()
            pass
        case 3:
            huntAnimals()
            pass
        case 4:
            buildShelter()
        case 5:
            eatFood()
        case 6:
            drinkWater()
        case 7:
            sleep()
        case 8:
            print('Exitig the game...')
            break
        case _:
            print('Please Enter a valid choice...')

if not isAlive:
    print('Game Over.....')

