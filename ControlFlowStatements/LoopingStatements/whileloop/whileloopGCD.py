no1 = 48
no2 = 18
i = 1

if no1 > no2 : 
    i = no1
else : 
    i = no2

while True : 
    
    if no1 % i == 0 and no2 % i == 0 : 
        break
    i -= 1

print("GCD :", i)

