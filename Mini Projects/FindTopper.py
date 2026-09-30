students = {"bhavik":[20,30,40],"raj":[22,33,55],"jay":[22,34,67],"kunal":[18,19,22]}
toppers= None
max = 0

for i,j in students.items():
    print(i," ",sum(j)/len(j))
    avg = sum(j)//len(j)
    if avg>max:
        max = avg
        toppers = i

print("topper...",toppers)        
