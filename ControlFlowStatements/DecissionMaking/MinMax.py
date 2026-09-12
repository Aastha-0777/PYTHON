no1 = int(input('Enter the Value of Number 1 : '))
no2 = int(input('Enter the Value of Number 2 : '))

if no1 > no2 :
    min, max = no2, no1
else : 
    min, max = no1, no2

print(f'Max : {max} and Min : {min}')