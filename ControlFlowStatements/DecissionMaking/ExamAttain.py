ataindance = float(input('Enter the Ataindace Percentage : '))
assignmentNo = int(input('Enter the No. of Assignment Submited : '))

if (ataindance > 90 and assignmentNo == 8) or (ataindance > 50 and assignmentNo == 20) :
    print('You can Give the Exam')
else : 
    print('You can not Give the Exam')
