def getValues(**kwargs):

    sum = 0

    for j in kwargs.values():

        if type(j) == int :

            sum += j
        else:

            return 0

    return sum


print(getValues(a = 60, b = 7))
