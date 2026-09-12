#empty set
data = set({}) #empty set
print(data)
print(type(data))


data  = {"mon","tue","wed","thu"}
print(data)
# print(data[0])

# for i in range(0,len(data)):
#     print(data[i])

# for i in data:
#     print(i)


#element..

data.add("jan")    
print(data)

data.update(["netflix","shaadi.ccom"])
print(data)
data.update("horror")
print(data)


#remove
# removedELm = data.pop()
# print("removing...",removedELm)
# print(data)   


data.remove("mon")
print(data)