correctNum = 25

while True : 
    userNum = int(input('Enter a Number : '))
    if correctNum == userNum : 
        print('Hurrey!! You Have Gussed it Correctly.')
        break
    elif correctNum > userNum :
        print('Number is TOO SMALL.Plese Try Again.') 
        continue
    elif correctNum < userNum : 
        print('Number is TOO BIG.Plese Try Again.')
        continue

