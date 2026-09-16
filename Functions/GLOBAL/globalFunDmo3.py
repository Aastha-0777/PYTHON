nums = [11,23,3,45,6,90,123,567,-9012,1]

#x = sorted(nums)
x = sorted(nums,key=abs)
print(x)
x1 = sorted(nums,key=abs,reverse=True)
print(x1)


#string

names = ["raj","jal","jay","jap","parth","kunal","zara","amit","laxmi"]
x2 = sorted(names)
print(x2)

#cust --> len 
x3 = sorted(names,key=len)
print(x3)


#tuple..
users = [("aman",23),("raj",21),("parth",24)]
# x4 = sorted(users)
# print(x4)
x4 = sorted(users,key=lambda x:x[1])
x4 = sorted(users,key=lambda x:x[1],reverse=True)
print(x4)