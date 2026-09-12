data = ["naman","jay","racecar","a","bob","jay","madam"]
print(data)
palindromeList = ["palindrome" if i == i[::-1] else "not palindrome" for i in data]
print(palindromeList)