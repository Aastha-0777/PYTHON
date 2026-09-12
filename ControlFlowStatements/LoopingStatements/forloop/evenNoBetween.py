startingPoint = int(input("Enter the Starting Point : "))
endingPoint = int(input("Enter the Ending Point : "))


# if startingPoint > endingPoint : 
#     for i in range(endingPoint, startingPoint + 1) : 
#         if i % 2 == 0 : 
#             print(i)
# else : 
#     for i in range(startingPoint, endingPoint + 1) : 
#         if i % 2 == 0 : 
#             print(i)

i = 1

if startingPoint > endingPoint : 
    i = -1

for i in range(startingPoint, endingPoint + i, i) : 
       if i % 2 == 0 : 
        print(i)

