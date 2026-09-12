x = 67


def change():

    global x
    print(f'x before changing : {x}')
    x = 6767
    print(f'x after changing : {x}')


print(f'x before change called : {x}')

change()

print(f'x after change called : {x}')
