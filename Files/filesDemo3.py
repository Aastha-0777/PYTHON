#read 
#file must be there to read..

# file = open('./Files/taks1.txt', 'r')
# data = file.read()
# print(data)
# file.close()

# to read specific char then pass it as args in read() function
# file = open('./Files/taks1.txt', 'r')
# data = file.read(7)
# print(data)
# file.close()

# #readline() will read the one line at a time
# file = open('./Files/taks1.txt', 'r')
# data = file.readline()
# print(data)
# file.close()

#to read the hole file using readline() func
# count = 0
# file = open('./Files/taks1.txt', 'r')
# while True : 
#     data = file.read()
#     print(data)
#     count+=1
#     if not data : 
#         break

# file.close()
# print(count)


# file = open('./Files/taks1.txt', 'r')
# data = file.readlines()
# print(data)
# file.close()

file = open('./Files/taks1.txt', 'r')

for i in file.readlines() : 
    print(i, end='')

file.close()
