def sum(*args) : 

    sum = 0

    for i in args : 
        sum += i

    print(f'sum : {sum}')

def diff(*args) : 

    diff = -1

    for i in args : 
        diff -= i

    print(f'diff : {diff}')

def product(*args) : 
    
    product = 1

    for i in args : 
        product *= i

    print(f'product : {product}')
            
def div(*args) : 
    
    div = 1

    for i in args : 
        div /= i

    print(f'div : {div}')

def cal(func, *args) : 

    func(*args)

op = input('Enter the Operator : ')

if op == '+' : 
    cal(sum, 60, 7)
elif op == '-' :
    cal(diff, 70, 4)
elif op == '*' : 
    cal(product, 7, 100)
else :
    cal(div, 50, 4)

