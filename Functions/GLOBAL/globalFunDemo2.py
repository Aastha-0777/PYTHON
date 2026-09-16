#all , any

marks = [21,22,23,24,21]

res = all(i>=20 for i in marks)
print(res)

names = ["rama","sushma","krishna","ganesha","jaya","preeti"]

res1 = all(i.endswith("a") for i in names)
print(res1)

#any..

res3 = any(i.endswith("i") for i in names)
print(res3)