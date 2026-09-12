nos = [1,2,3,4,5]
nos2=[]

for i in nos : 
    nos2.append(i**2)

print(nos2)

nos3 = [i**2 for i in nos]
print(nos3)

nos4 = map(lambda num : num**2, nos) #it returns a object...
#nos4 is a object...
print(list(nos4))

names = ["raj","parth","amit"]
uppername =[]

for i in names : 
    uppername.append(i.upper())

print(uppername)

uppername2 = [i.upper() for i in names]
print(uppername2)

uppername3 = map(lambda name : name.upper(), names)
print(tuple(uppername3))

sales = [100,200,300,400]
salesp = []

for i in sales :
    salesp.append(i * 1.1)

print(salesp)

#comprehesion is more powerfull than map
salesp2 = [i*1.1 for i in sales]
print(salesp2)

salesp3 = map(lambda sal : sal*1.1, sales)
print(list(salesp3))