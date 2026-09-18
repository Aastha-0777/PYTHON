# file = open('./Files/Demo2Apd.txt', 'a')
# file.write('Hello this is Append Mode\n')
# file.close()

file = open('./Files/Demo2Apd.txt', 'a')

name = 'Vasudev'
age = 19

file.write(f'Name : {name} Age : {age}\n')
file.close()