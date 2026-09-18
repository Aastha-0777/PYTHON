file = open('./Files/taks1.txt', 'w')
data  = {"id":1,"name":"raj","age":23}

keys = data.keys()

res = [data[i] for i in keys]
print(res)

for i,j in data.items() :
    file.write(f'{i} : {j}\n')