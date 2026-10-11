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

# ---------------------------- GAME SETTINGS ----------------------------
# Change these numbers to make the game easier or harder.
STORM_CHANCE = 20        # % chance that a storm blocks an outdoor action
ACTIONS_PER_DAY = 3      # actions you must do before you are allowed to sleep
LOOT_MAX = 3             # most items one search can find (per item type)
FOOD_RESTORE = 5         # hunger % restored by eating one Food
WATER_RESTORE = 5        # thirst % restored by drinking one Water
HEAL_AMOUNT = 7          # health restored by eating one Food
SHELTER_WOOD = {1: 10, 2: 20, 3: 35}          # wood needed for each shelter size
BOSS_STORM_DAMAGE = {1: 75, 2: 45, 3: 15}     # Day 10 storm damage by shelter size


stats = {'Health': 100, 'Food': 3, 'Water': 3, 'Wood': 0}
itemsCouldBeFound = ['Food', 'Wood', 'Water']
hungerCounter = 100      # in percent
thirstCounter = 100      # in percent
dayCounter = 1
actionsToday = 0
haveShelter = False
shelterLevel = 0         # 0 = none, 1 = A-Frame, 2 = Lean-To, 3 = Log Cabin
isAlive = True


def clear_screen():
    print("\033[H\033[J", end="")


def askNumber(prompt):
    # Returns the number typed, or -1 if the player typed something else
    try:
        return int(input(prompt))
    except ValueError:
        return -1


# ------------------------------- STORY ---------------------------------

def beforeStory():

    print('=================================== BEFORE STORY ===================================')
    time.sleep(1)
    print('You (THINKING) : Ah! What a great day.\n\tFinally going back home after a long Time..')
    time.sleep(2.5)
    print('You (THINKING) : I will give surprise to my family \n\tand we will celebrate the New Year Together....')
    time.sleep(2.5)
    print('Wait What..!! What is happening...')
    time.sleep(2.5)
    print('The Radar started Fluctuating...')
    time.sleep(2.5)
    print('The engine blew up, sending the plane diving fast toward a strange jungle island.')
    time.sleep(2.5)
    print('The plane tore open, and everyone put on oxygen masks as bags flew everywhere.')
    time.sleep(2.5)
    clear_screen()
    time.sleep(2)
    print('BHOMMM..')
    time.sleep(2)
    print('The Plane Crashed!!!')
    time.sleep(2.5)


def afterCrash():

    clear_screen()
    print('=================================== AFTER CRASH ===================================')
    time.sleep(2)
    print('You woke up alone on a dark beach next to the broken pieces of the plane.')
    time.sleep(2.5)
    print('You (THINKING) : What happened and how it happened...')
    time.sleep(2.5)
    print('You Saw Your Watch..\n\tGlass Broken, Showing 17th Dec.')
    time.sleep(2.5)
    print('You Realised that a Patrolling Helicopter will Come for patrolling after 10 days...')
    time.sleep(2.5)
    print('So Now You have to Survive in this Island For 10 days....')
    time.sleep(1.5)
    clear_screen()


def finalDay():

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


def hitStorm():
    return random.randint(1, 100) <= STORM_CHANCE


def stormDamage():
    print('The storm batters you!')
    stats['Health'] -= random.randint(5, 15)


def healthManager():
    # Every action makes the player hungrier and thirstier.
    # Once a meter is empty, the player starts losing health.

    global thirstCounter, hungerCounter

    if thirstCounter > 0:
        thirstCounter = max(0, thirstCounter - random.randint(1, 8))
    else:
        stats['Health'] -= random.randint(1, 11)

    if hungerCounter > 0:
        hungerCounter = max(0, hungerCounter - random.randint(1, 8))
    else:
        stats['Health'] -= random.randint(1, 11)


def endAction():
    # Call this once after every action that takes time.

    global isAlive, actionsToday

    actionsToday += 1
    healthManager()
    if stats['Health'] <= 0:
        stats['Health'] = 0
        isAlive = False
        print('You Died Challenging...\nWell Played Player!!')
    elif hungerCounter <= 35 or thirstCounter <= 35:
        print('Warning! You are weak from hunger or thirst...')


# ------------------------------ ACTIONS --------------------------------

def searchIsland():

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Searching Island in the Storm....')
        stormDamage()
        endAction()
        return

    print('Searching Island....')
    time.sleep(3)
    endAction()
    if not isAlive:
        return

    foundList = random.choices(
        itemsCouldBeFound, k=random.randint(1, len(itemsCouldBeFound)))
    foundSomething = False
    for i in foundList:
        amount = random.randint(0, LOOT_MAX)
        if amount > 0:
            stats[i] += amount
            print(f'{amount} {i} Found...')
            foundSomething = True
    if not foundSomething:
        print('Found Nothing on this part of the Island...')
        return


def collectWood():

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Collecting Wood in the Storm....')
        stormDamage()
        endAction()
        return

    print('Collecting Woods...')
    time.sleep(3)
    woodAmount = random.randint(1, 21)
    endAction()
    if not isAlive:
        return
    stats['Wood'] += woodAmount
    print(f'You Collected {woodAmount} Woods....')


def huntAnimals():

    if hitStorm() or dayCounter == 10:
        print('You Can\'t Go For Hunting in the Storm....')
        stormDamage()
        endAction()
        return

    clear_screen()
    print('SEARCHING......')
    time.sleep(3)
    print('Animal Found...')

    animalHealth = random.randint(35, 101)

    while animalHealth > 0:

        print('Attacking....')
        animalHealth -= random.randint(1, 21)
        stats['Health'] -= random.randint(1, 5)
        print('The animal hits back!')
        endAction()
        if not isAlive:
            return

    foodAmount = random.randint(1, 11)
    stats['Food'] += foodAmount
    print(f'Eureka You Killed the Animal.. \n\t You got {foodAmount} Amount of Food')


def tryBuild(level, name):

    global haveShelter, shelterLevel

    if level <= shelterLevel:
        print('You already have a shelter this good or better...')
        return
    if stats['Wood'] < SHELTER_WOOD[level]:
        print('You Don\'t have enough Wood to Build this shelter....')
        return

    print(f'Building {name}...')
    stats['Wood'] -= SHELTER_WOOD[level]
    haveShelter = True
    shelterLevel = level
    endAction()


def buildShelter():

    if hitStorm():
        print('You can not build Shelter in Storm...')
        stormDamage()
        endAction()
        return

    print(f'1. A-Frame Tarp Shelter (Small)  - {SHELTER_WOOD[1]} wood')
    print(f'2. Lean-To Brush Hut (Medium)    - {SHELTER_WOOD[2]} wood')
    print(f'3. Log Cabin Box (Large)         - {SHELTER_WOOD[3]} wood')
    shChoice = askNumber('What Type of Shelter You Want to Build : ')

    match shChoice:

        case 1:
            tryBuild(1, 'A-Frame Tarp Shelter')
        case 2:
            tryBuild(2, 'Lean-To Brush Hut Shelter')
        case 3:
            tryBuild(3, 'Log Cabin Box Shelter')
        case _:
            print('Please Enter a valid Choice')


def eatFood():

    global hungerCounter

    if stats['Food'] <= 0:
        print('You Don\'t have Enough Food to Eat...')
        print('Please Search Island or Hunt For More Food...')
        return

    # Eating also heals, so it is allowed when hurt even if hunger is full
    if hungerCounter >= 100 and stats['Health'] >= 100:
        print('You Are Full and Healthy...')
        return

    print('Eating Food....')
    hungerCounter = min(100, hungerCounter + FOOD_RESTORE)
    stats['Food'] -= 1
    if stats['Health'] >= 100:
        print('Your Health is Full...')
    else:
        stats['Health'] = min(100, stats['Health'] + HEAL_AMOUNT)
        print(f'Health Increased By +{HEAL_AMOUNT}....')


def drinkWater():

    global thirstCounter

    if stats['Water'] <= 0:
        print('You Don\'t have Enough Water to Drink...')
        print('Please Search Island For More Water...')
        return

    if thirstCounter >= 100:
        print('You Can Not Drink More Water...')
        return

    print('Drinking Water....')
    thirstCounter = min(100, thirstCounter + WATER_RESTORE)
    stats['Water'] -= 1


def sleep():

    global dayCounter, actionsToday, isAlive

    if not haveShelter:
        print('To Sleep Securely You have to build a Shelter!!')
        return

    if actionsToday < ACTIONS_PER_DAY:
        print(f'You are not tired yet. Do {ACTIONS_PER_DAY - actionsToday} more action(s) first.')
        return

    if dayCounter == 10:
        # Boss challenge: the bigger your shelter, the less the storm hurts
        print('The massive storm hits during the night!')
        time.sleep(2)
        stats['Health'] -= random.randint(5, 15) + BOSS_STORM_DAMAGE[shelterLevel]
        if stats['Health'] <= 0:
            stats['Health'] = 0
            isAlive = False
            print('Your shelter could not protect you from the storm...')
            return
    else:
        print('---SWEET DREAMS---')

    dayCounter += 1
    actionsToday = 0


# ------------------------------ MAIN LOOP ------------------------------

def main():

    beforeStory()
    afterCrash()

    print('---------- WELCOME TO ISLAND SURVIVAL CHALLENGE ----------\n\n')

    while isAlive:

        if dayCounter == 11:
            finalDay()
            break
        if dayCounter == 10:
            print('------------------------------ FINAL DAY ------------------------------')
            print('A massive storm is coming tonight. The bigger your shelter, the better your chances.\n')

        print(f'========= DAY : {dayCounter} =========\n')

        print(f'Your Details : {stats}')
        print(f'Hunger Percent : {hungerCounter}%')
        print(f'Thirst Percent : {thirstCounter}%')
        print(f'Actions Today : {min(actionsToday, ACTIONS_PER_DAY)}/{ACTIONS_PER_DAY}\n')

        print('--------------------- OPTIONS ---------------------')
        print('1. Search the island for food and water.')
        print('2. Collect wood to build a shelter.')
        print('3. Hunt animals for food.')
        print('4. Build The Shelter.')
        print('5. Eat Food.')
        print('6. Drink Water.')
        print('7. Sleep.')
        print('8. Quit')
        choice = askNumber('What Would you like to do next? : ')

        match choice:

            case 1:
                searchIsland()
            case 2:
                collectWood()
            case 3:
                huntAnimals()
            case 4:
                buildShelter()
            case 5:
                eatFood()
            case 6:
                drinkWater()
            case 7:
                sleep()
            case 8:
                print('Exiting the game...')
                break
            case _:
                print('Please Enter a valid choice...')

    if not isAlive:
        print('Game Over.....')


if __name__ == '__main__':
    main()