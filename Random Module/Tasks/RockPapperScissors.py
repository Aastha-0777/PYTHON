import random

gamechoices = ['rock', 'paper', 'scissors']
records = {'userCount' : 0}


while True:

    print("------ ROCK PAPER SCISSORS ------")
    userChoice = input('Enter Your Choice : ').lower()

    compChoice = random.choice(gamechoices)

    if userChoice == compChoice:
        print(f'Comp Choice : {compChoice}')
        print('Its a Tie..')
    elif (compChoice == "paper" and userChoice == "rock") or (compChoice == "scissor" and userChoice == "paper") or (compChoice == "rock" and userChoice == "scissor"):
        print(f'Comp Choice : {compChoice}')
        print('You Lost...')
        records['userCount']=records['userCount']+1    
    else:
        print(f'Comp Choice : {compChoice}')
        print('You Win...')

    reply = input('Do You Want to Play Again ? (y/n) : ').lower()
    if reply == 'n' : 
        break

print(records)


