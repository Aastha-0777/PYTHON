#create a function accept kwargs as argument, return only keys and print it

def getDetails(**kwargs) : 

    return kwargs.keys()

print(getDetails(name = "Vasudev", age = "19", hoby = "football"))