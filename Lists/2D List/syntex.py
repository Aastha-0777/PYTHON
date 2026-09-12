sales = [[30, 50, [90]], [20, 67, [77]], [50, 22, [88]]]

print(sales)
print(sales[1])
print(sales[1][1])

#range loop

# for i in range(0, len(sales)) : 
#     print(sales[i])
#     for j in range(0, len(sales[i])) : 
#         print(sales[i][j], end= " ")

#     print() 

# for i in sales : 
#     print(i)
#     for j in i : 
#         print(j, end=" ")

#     print()

# for i,j in sales :
#     print(i, " ", j)

for i in sales : 
    print(i)
    for j in i : 
        print(j, end=" ")
        for k in j : 
            print(k, end="")

