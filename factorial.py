# Write a program to find the factorial of a number. Factorial of a non-negative integer is the multiplication of all integers smaller than or equal to n


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


user_input = int(input("Enter the number to find factorial"))
fact = factorial(user_input)
print("Factorial of %s is %s " % (user_input, fact))
