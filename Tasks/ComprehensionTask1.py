# 1. Odd Number Detector
# Create a list of odd numbers from 1 to 50 using list comprehension.
# Expected output: [1, 3, 5, 7, ...]

oddNumList = [i for i in range(1, 51) if i % 2 != 0]

print("Odd Number List : ", oddNumList)
