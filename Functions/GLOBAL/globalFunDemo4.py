#zip
a = [1,2,3]
b = [11,22,33]
c = [100,200,300]

for i,j,k in zip(a,b,c):
    print(i,j,k)

data = {}
for i,j in zip(a,b):    
    data[i]=j

print(data)    
