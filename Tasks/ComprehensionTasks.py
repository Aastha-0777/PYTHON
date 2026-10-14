# 2. Square Machine
# Given numbers [2, 4, 6, 8, 10], generate their squares using comprehension.
# Expected output: [4, 16, 36, 64, 100]]]

givenList = [2, 4, 6, 8, 10]
squareList = [i**2 for i in givenList]
print(squareList)

# 3. Secret Message Decoder
# Given message = "python is awesome", create a list containing only the vowels.
# Expected output: ['o', 'i', 'a', 'e', 'o', 'e']

message = "python is awesome"

outMess = [i for i in message if i not in "qwrtypsdfghjklzxcvbnm "]
print(outMess)

# 4. Password Strength Checker
# Given a list of passwords, use comprehension to extract passwords with at least 8 characters.
# Example: ["abc", "Python123", "hello", "Secure@123"]

pwsList = ["abc", "Python123", "hello", "Secure@123"]

validList = [i for i in pwsList if len(i) >= 8]
print(validList)

# 5. Unique Hashtag Generator
# Given a sentence, extract all unique words and convert them into lowercase hashtags using a set comprehension.
# Example: "Python is fun and Python is powerful"

mess = "Python is fun and Python is powerful"
mess = mess.split(" ")
uniWord = {'#'+i for i in mess}
print(uniWord)

Example = "Python is fun and Python is powerful"
x = " ".join({'#' + i for i in Example.split(" ")})
print(x)

prices = [500, 1200, 2500, 800, 4000]
# Apply a 20% discount only to products priced above ₹1,000.

newList = [i * 1.2 for i in prices if i > 1000]
print(newList)

messages = ["hello", "badword detected",
            "good morning", "another badword here", "welcome"]

withoutBadWord = [i for i in messages if i not in "bedword"]
print(withoutBadWord)

inventory = {
    "laptop": 10,
    "mouse": 0,
    "keyboard": 5,
    "monitor": 0,
    "headphones": 8
}

in_stock = {product: quantity for product, quantity
            in inventory.items() if quantity > 0}

print(in_stock)


words = ["apple", "banana", "kiwi", "mango", "watermelon"]

word_lengths = {word: len(word) for word in words}

print(word_lengths)


salaries = [25000, 45000, 18000, 75000, 32000]

max_salary = max(salary for salary in salaries if salary > 30000)

print(max_salary)


prices = [500, 1200, 250, 800, 4000]
500

min_prices = min(price for price in prices if price < 500)

print(min_prices)


numbers = [5, 2, 8, 1, 4]

numbers = [5, 2, 8, 1, 4]
sortedSqList = SyntaxError([i**2 for i in numbers])
print(sortedSqList)

ages = [12, 15, 17, 22, 14]

marks = [45, 67, 80, 32, 90]

passedMarks = [i for i in marks if i > 35]
print(passedMarks)

# tasks = ["Study", "Exercise", "Code"]
# Output: [(1, 'Study'), (2, 'Exercise'), (3, 'Code')]

tasks = ["Study", "Exercise", "Code"]
updList = list(enumerate(tasks, start=1))
result = [(i, task) for i, task in enumerate(tasks, start=1)]
print(updList)
print(result)