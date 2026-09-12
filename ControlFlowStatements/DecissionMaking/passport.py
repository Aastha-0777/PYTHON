#to issue a passport user must have aadhar card and zero crimnal offence and must be indian c

isAddhar = bool(input('Do You have a Addhar Card : (True/False) '))
criminalOff = int(input('Enter the Number of Criminal Offence You Have : '))
isIndianCitizen = bool(input('Are You a Indian Citizen : (True/False)'))

if isIndianCitizen :
    if criminalOff == 0 :
        if isAddhar : 
            print("You are Elligible For Passport!!")
        else : 
            print("You are not Elligible For Passport as you don't have addhar card")
    else : 
        print("You are not Elligible For Passport as you have cirminal offence")
else : 
    print("You are Elligible For Passport as you are not an Indian Citizen")


