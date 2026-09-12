# s = set(users)

# print("set Users : ", s)
users = ["amita","sumit","raj","neha","amita","sumit","kunal"]


s = {i[::-1] for i in users}

print(s)
