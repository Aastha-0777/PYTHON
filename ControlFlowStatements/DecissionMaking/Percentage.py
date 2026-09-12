per_10 = float(input('Enter Your 10th Percentage : '))
per_12 = float(input('Enter Your 12th Percentage : '))

if per_10 > 80 : 
    if per_12 > 75 :
        print('You can take admition!!')
    else :
        print('You can not take Admition due to low per. in 12th')
else : 
    print('You can not take Admition due to low per. in 10th')

