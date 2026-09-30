# Marks Analyzer: Take 5 students' marks in a list.
# Print highest,
# lowest,
# average, 
# and how many passed (marks >= 35)

marks = []

for i in range(1, 6) : 

    mark = int(input(f'Enter the Mark of Student {i} : '))
    marks.append(mark)

maxMark = max(marks)
print(f'Max Marks = {maxMark}')

minMark = min(marks)
print(f'Min Marks = {minMark}')

avgMark = sum(marks) / len(marks)
print(f'Avg Marks = {avgMark}')

conter = 0
for i in marks : 

    if i >= 35 : 
        conter+=1

print(f"No Of Students who Passed : {conter}")


