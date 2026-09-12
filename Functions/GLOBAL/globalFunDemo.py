# nums = [10, 20, 30, 40, 50, 67, -10, -20, 22]

# print(min(nums))
# print(max(nums))
# print(abs(-1))

# print('------------------------')

# print(min(nums, key=abs))
# print(max(nums, key=abs))

# names= ["raj","zara","amit","parth","sumit"]

# print('------------------------')

# print(min(names))
# print(max(names))

# print('------------------------')

# print(min(names, key=len))
# print(max(names, key=len))

# print('------------------------')

# users = [("Sam",23),("Raj",25),("Jay",26),("Amit",28)]
# #users = [(29,"Sam"),(25,"Raj"),(26,"Jay"),(28,"Amit")]

# print(min(users))

# print('------------------------')

# users = [(29,"Sam"),(25,"Raj"),(26,"Jay"),(28,"Amit")]

# print(min(users))

# ans = min(users, key= lambda x : x[1])

# print('------------------------')

# print(ans)


nums = [1,2,3,4,5]
print('summ...', sum(nums))

#sum func
#do sum of only evn no:

# evenSum = sum(i for i in nums if i % 2 == 0)
# print(evenSum)

# #sales greater than 300

# sales = [100,200,23,400,50,67,900]

# sum300 = sum(i for i in sales if i>300)
# print(sum300)

# #square of sum
# data = [1,2,3,4,5]

# sqSum = sum(i**2 for i in data)
# print(sqSum)

# #cube sum

# data= [1,5,3]

# cubSum = sum(i**3 for i in data)
# print(cubSum)

# #len sum
# data = ["raj","parth","ok"]

# lenSum = sum(len(i) for i in data)
# print(lenSum)

#dict:
students = [
    {"id":1,"name":"raj","marks":23},
    {"id":2,"name":"jay","marks":25},
    {"id":3,"name":"parth","marks":20}
]

# res = sum(i for i in students) --> will give error 'cause it takes 0th inx as default

res = sum(i['marks'] for i in students)
print(res)