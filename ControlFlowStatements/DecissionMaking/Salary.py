#user salary 12000
#display salary:
#1000000 PA tax 20%
#700000 pa tax 10%
#500000 pa tax 5%
#200000 pa tax 2%

#net salary

salary = float(input("Enter the Monthly Salary : "))

yearly_salary = salary * 12

if salary == 1000000 : 
    tax = 20
elif salary == 700000 : 
    tax = 10
elif salary == 500000 :
    tax = 5
else :
    tax = 2

net_salary = yearly_salary - (yearly_salary / 100 * tax)

print(f'Net Salary : {net_salary}')

