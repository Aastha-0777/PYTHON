# sales = [[30, 50], [20, 67], [50, 22]]
# totalSales = []
# sum = 0

# for i in sales : 
#     for j in i : 
#         sum += j
#     totalSales.append(sum)
#     sum = 0

# print(totalSales)

sales = [["MON", 30, 50], ["TUE", 20, 67], ["WED", 50, 22]]

maxSales = 0
totalSales = []
dayList = []
final 
sum = 0

for i in sales :
    dayList.append(i[0]) 
    for j in i[1 : 3] : 
        sum += j
    totalSales.append(sum)
    sum = 0

print(totalSales)
print(dayList)

maxSales = totalSales[0]
for i in totalSales : 
    if i > maxSales : 
        maxSales = i

print(maxSales)