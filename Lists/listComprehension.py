data = [10 , 20, 30, 40, 50, 60]

print(data)

newData = [i + 7 for i in data]

print(newData)

data = ["naman","jay","racecar","a","bob","jay","madam"]
print(data)
palindromeList = [i for i in data if i == i[::-1]]
print(palindromeList)