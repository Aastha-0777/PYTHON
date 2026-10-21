# def countNum (count) :
#     print(count)
#     count += 1
#     if(count > 10) : 
#         return
#     countNum(count)
    

# countNum(1)

# def digitCount(num) :
    
#     if(num != 0) :
#         num /= 10
#         count += 1
#         digitCount(num)
#     return count

# count = digitCount(1234)
# print(count)

#print sum of digit using recursion

# def digitSum(no) : 

#     if no == 0 :
#         return 0
#     return int(no%10 + digitSum(no/10))

# print(digitSum(123))


#print all factors of number

def printAllFac(no, i) : 

    if i > no :
        return

    if no % i == 0 :
        print(i)
        i += 1
        printAllFac(no, i)

printAllFac(12, 1)