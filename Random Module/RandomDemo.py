import random

# print(random.random()) #it will genereate nums between 0-1
# print(random.random() * 100) # but we can use it like this too

# print(random.randint(1, 101)) # u can give para for range end is exclusive
# print(random.randrange(1, 101, 10)) #similar to randint but you can specify the steps
# print(random.uniform(1, 20)) # randint alternative for float values

colours = ["red", 'black', 'blue', 'brown', 'pink', 'yellow', 'orange']

print(f'colours : {colours}')
print(random.choice(colours))
print(random.choices(colours))
print(random.sample(colours))