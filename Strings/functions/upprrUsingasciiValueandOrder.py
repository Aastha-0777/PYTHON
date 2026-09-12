# ord() and char()

string = input("Enter a String in lower case : ")
upperStr = ""

for i in string:

    if ord(i) >= 97 and ord(i) <= 122:
      upperStr = upperStr + chr(ord(i) - 32)
    else:
       upperStr = upperStr + i

print(f'Upper String : {upperStr}')
    
      