data = {1:"amit",2:22,3:33,4:"raj",5:None,6:["parth","sumit"],7:89}
numData = {}

for i,j in data.items() : 

    if type(j) == int or type(j) == float :
        numData[i] = j

print(numData)
