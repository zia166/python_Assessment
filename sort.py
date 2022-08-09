# Write a program to sort three numbers.

num = input("Enter the number")
num = num.split()
num1 = [int(i) for i in num]
num1.sort()
print(num1)
