def demoFun(*args):

    for i in args:

        if type(i) == "str":
            return True
        else:
            return False

print(demoFun("str", 33))

