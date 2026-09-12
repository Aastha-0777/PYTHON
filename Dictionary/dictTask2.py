data= {1:"naman",2:"raj",3:"bob",4:"jay"} 
palindromData = {}

for i,j in data.items() :
    if j == j[::-1] : 
        palindromData[i] = j

print(palindromData)     