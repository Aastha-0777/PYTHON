no = [1, 2, 3, 4, 5, 6]

k = 4

print(no[-1 : -(k + 1) : -1] + no[0 : len(no) - k])