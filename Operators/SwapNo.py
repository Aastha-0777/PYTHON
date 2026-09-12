no1 = int(input('Enter the Value of Num1 : '))
no2 = int(input('Enter the Value of Num2 : '))

temp = no1
no1 = no2
no2 = temp

print(f'Num1 after swaping : {no1}, Num2 after swaping : {no2}')

no1 = int(input('Enter the Value of Num1 : '))
no2 = int(input('Enter the Value of Num2 : '))

no1 = no1 + no2 
no2 = no1 - no2
no1 = no1 - no2

print(f'Num1 after swaping : {no1}, Num2 after swaping : {no2}')

# special feature of python

a, b, c = 10, 20, 30;

print(f'a : {a} , b : {b} , c : {c}')

no1 = int(input('Enter the Value of Num1 : '))
no2 = int(input('Enter the Value of Num2 : '))

no1, no2 = no2, no1

print(f'Num1 after swaping : {no1}, Num2 after swaping : {no2}')
