sales = [100,200,300,400]

sales250 = [i for i in sales if i > 250]
print(sales250)

sales250_2 = list(filter(lambda x : x > 250, sales))
print(sales250_2)

names = ["rama","rekha","jaya","sushma","nirma"]

namesr = list(filter(lambda x : 'r' in x, names))
print(namesr)

nums = [100,200,300,400, 111, 676, 28, 555]

namsp = list(filter(lambda x: str(x) == str(x)[::-1], nums))
print(namsp)