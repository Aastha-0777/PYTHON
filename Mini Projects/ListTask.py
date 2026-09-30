# data = ["raj","jay","parth","kunal"]

# # p1:["kunal","parth","jay","raj"]
# # p2:["lanuk","htrap","yaj","jar"]

# print(data)
# # p1 = data.reverse()
# p1 = [data[i][::-1] for i in range(len(data)-1, -1, -1)]
# print(p1)

# # p2 = [i[::-1] for i in data]
# # print(p2)


users = {"amit":["react","js","java","python"],"kunal":["js","python"]}

commonHobby = set(users["amit"]) & set(users["kunal"])
print(commonHobby)