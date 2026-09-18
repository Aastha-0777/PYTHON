file = open('./Files/demo1.txt', 'r')

# count = 0

# for i in file.readlines() :

#     print(i, end="")
#     count+=1
#     if(count == 10) :
#         break

# count = 0
# data = file.readline()

# for i in data :

#     if i == "" or i == " " or i == "\n" :
#         continue
#     else :
#         count += 1

# print(count)

# print(data)

# count = 0
# data = file.readline()

# words = len(data.split(" "))
# print(words)

# count = 0
# words = 0
# while True :

#     data = file.readline()
#     words += len(data.split(" "))
#     if not data :
#         break

# print(words)

data = file.read()
x = data.split()
p1 = [i for i in x if i == i[::-1]]
print(p1)