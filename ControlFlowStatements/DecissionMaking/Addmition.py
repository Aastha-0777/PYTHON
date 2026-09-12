math = float(input('Entet Your Math Marks : '))
physics = float(input('Entet Your Physics Marks : '))
chem = float(input('Entet Your Chem Marks : '))

total = math + physics + chem

if total >= 250 or math >= 90 : 
    print('You are Elegible')
else : 
    print('You are not Elegible')

