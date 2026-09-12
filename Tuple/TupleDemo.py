# data = ()
# print(data)
# print(type(data))

data = ("aastha","vasudev","raj","amit")
print(data)
print(data[0])

# range
for i in range(0,len(data)):
    print(data[i],end=" ")

for i in data:
    print(i) 

#typeError: 'tuple' object does not support item assignment
#data[0] = "AMITA"

ind =data.index("raj")
print("index = ",ind)