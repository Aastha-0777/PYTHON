def userDetails(name, age, salary) : 

    print(f'Name : {name} Age : {age} Salary : {salary}')


userDetails('Vasudev', 19, 1234567)

#keyword arrgument 

userDetails(name='Vasudev', salary=1234567, age=19)
#userDetails(name='Vasudev', salary=1234567, 19) --> compiletime error 
userDetails('Vasudev', salary=1234567, age=19)
#userDetails(name='Vasudev', salary=1234567, name='Aastha') --> runtime error

