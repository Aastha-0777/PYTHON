data = ["naman","jay","racecar","a","bob","jay","madam"]

newData = []

print(data)

for i in data : 

    if i == i[::-1] : 
        newData.append(i)

print(newData)