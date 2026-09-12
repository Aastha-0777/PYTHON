# def test() : 
#     print('Test')

# test()

x = lambda : print('Test')

y = x()

print(y)

#lambda function

#withou return type without argumen
# def test():
#     print("test")
# test()    

test = lambda :print("test")
test()

#with arg no return type..
# def add(a,b):
#     print(a+b)
# add(10,20)    

add = lambda a,b:print(a+b)
add(60,7)

#with argument with return type
# def fullname(fname,lname):
#     return f"{fname}  {lname}"

# x = fullname("virat","kohli")
# print(x)

fullname = lambda fname,lname : f"{fname} {lname}"
x = fullname("Cristiano","Ronaldo")
print(x)
print(fullname("Neymar","Jr."))

