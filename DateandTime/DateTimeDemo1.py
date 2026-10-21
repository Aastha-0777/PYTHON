import datetime

print(datetime.datetime.now()) #gives date and time 
print(datetime.date.today()) #gives system's data

d = datetime.date(2007, 4, 4)
t = datetime.time(14, 2, 24)

print(d)
print(t)

dt = datetime.datetime(2007, 7, 7, 7, 7, 7)
print(dt)

now = datetime.datetime.now()

print(f'Year : {now.year}')
print(f'Month : {now.month}')
print(f'Day : {now.day}')

#formate

#to convert date to string..

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%d-%m/%Y"))
print(now.strftime("%d-%m-%y"))
print(now.strftime("%d-%b-%y")) 
print(now.strftime("%A"))
print(now.strftime("%a"))
print(now.strftime("%B"))
print(now.strftime("%H"))
print(now.strftime("%I"))
print(now.strftime("%S"))
print(now.strftime("%p"))

#to convert string to date..

date_str = "25-12-26"

d = datetime.datetime.strptime(date_str,"%d-%m-%y")
print(d)


today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)
nextDay = today + datetime.timedelta(days=2)
nextWeek = today + datetime.timedelta(weeks=1, days=1)
nextHour = today + datetime.timedelta(hours=1)

print(today)
print(tomorrow)
print(nextDay)
print(nextWeek)
print(nextHour)

now = datetime.datetime.now()
nextHour = now + datetime.timedelta(hours=1)
print(nextHour)

diff = tomorrow - today
print(diff)
print(diff.days)

print(today<tomorrow)
print(today==tomorrow)
print(today>tomorrow)