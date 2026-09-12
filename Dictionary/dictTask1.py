data = {}

while True :

    key = input('Enter the Key : ')
    if key == 'exit' or key == 'Exit' or key == 'EXIT': 
        break
    else :
        value = input('Enter the Value : ')
        data[key] = value

print(data)    