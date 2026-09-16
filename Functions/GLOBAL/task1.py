students = [
    ("Rahul", 78),
    ("Amit", 92),
    ("Neha", 85),
    ("Priya", 95),
    ("Raj", 88)
]

print(max(students, key=lambda x : x[1])[0])