email = input('Enter an Email Id : ')
print(f'Entered Email : {email}')
print(f'Length of Entered Email : {len(email)}')
newEmail = ""

for i in email : 

    if i != " " : 
       newEmail += i

print(f'Correct Email : {newEmail}')
print(f'Length of Corrected Email : {len(newEmail)}')
