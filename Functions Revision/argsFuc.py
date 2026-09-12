# def getSum(*args):


#     flag = False
#     sum = 0
#     for i in args:

#         if type(i) != int:
#             flag = False
#             break
#         else:
#             sum+=i
#     return sum

# x = getSum(10, 20, 30, 40,50)
# print(x)


# def checkData(*args):

#     flag = False

#     for i in args :

#         if type(i) != int :
#             flag = False
#             break
#         else :
#             flag = True

#     return flag

# x  = checkData(10,20,30,"ok",40,50)
# print(x)

# def getUpperList(*args):

#     return [i.upper() for i in args if type(i) == str]

# x = getUpperList("ram","amit","sumit", 67)
# print(x)

def getPalindromes(*args):

    return [i for i in args if str(i) == str(i)[::-1]]

x = getPalindromes("naman",121,"raj","bob",22,23,"jay")
print(x)