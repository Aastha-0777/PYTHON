# def demo():
#     return "hello"
#     return "hi"

# d = demo()
# print(d)
def demo():
    yield 1
    yield 2
    yield 3

d = demo()
#print(d)    
# print(next(d))
# print(next(d))
# print(next(d))

for i in d:
    print(i)

def getData(sp,tnr,parts):

    yield [sp for sp in range(sp, tnr)]

g = getData(1, 100, 10)

print(next(g))


