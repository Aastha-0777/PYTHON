import random

gussedNum = random.randint(1, 501)

player1Guss = []
player2Guss = []

print('------ GUSS THE NUMBER ------')

while True:

    p1Num = int(input('Player 1 Enter Your Number : '))
    player1Guss.append(p1Num)

    if p1Num < gussedNum:
        print('Your Guss is too less...')
    elif p1Num > gussedNum:
        print('Your Guss is too high...')
    else:
        print('Eureka!! Player 1 You have Won the Game...')
        break

    p2Num = int(input('Player 2 Enter Your Number : '))
    player2Guss.append(p2Num)

    if p2Num < gussedNum:
        print('Your Guss is too less...')
    elif p2Num > gussedNum:
        print('Your Guss is too high...')
    else:
        print('Eureka!! Player 2 You have Won the Game...')
        break

print(f'Player 1 Guss : {player1Guss}')
print(f'Player 2 Guss : {player2Guss}')