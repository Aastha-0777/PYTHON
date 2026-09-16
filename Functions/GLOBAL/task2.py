# nums = [-15, 4, -2, 9, -7, 3]

# print(max(nums))

# names = ["Rahul", "Amit", "Neha", "Priya"]
# marks = [78, 92, 85, 95]

# x = list(zip(names, marks))

# print(x)
# print(min(x, key= lambda x : x[1])[0])

# movie = ["titanic","mirzapur","toxic","dhurandhar","aamir khan"]
# prices = [100, 250, 80, 450, 120]
# budget = 200


# print(min(x, key= lambda x : abs(x[1] - budget))[0])

products = [
    ("Laptop", 55000),
    ("Phone", 30000),
    ("Tablet", 20000),
    ("Watch", 15000),
    ("Headphone", 5000)
]

budget = 25000

x = [i for i in products if i[1] <= budget]
print(x)

print(max(x, key= lambda x : x[1]))