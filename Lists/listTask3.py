data = ["jay","ajay","raj","jay","parth","amit","parth","kunal"]
print(data)

uniData = []
dupData = []

for i in data : 

    if i not in uniData : 
        uniData.append(i)
    else : 
        dupData.append(i)

print(uniData)
print(dupData)