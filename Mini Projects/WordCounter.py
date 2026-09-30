# hi this is india and india is county
# {hi:1,this:1,is:2,india:2..}

sentence = input('Enter a Sentence : ')
senList = sentence.split(" ")

# count = senList.count("india")
# print(count)

countDict = dict({})

for i in senList : 

    countDict[i] = senList.count(i)
    # countDict[i] = countDict.get(0, i) + 1

print(countDict)