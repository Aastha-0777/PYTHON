sales = [[12, 30], [23, 67], [30, 90]]
print(sales)

_1DList = []
digitList = []
for i in sales : 
    _1DList.extend(i)

print(_1DList)

for i in _1DList : 
    (digitList.extend(str(i)))

print(digitList)