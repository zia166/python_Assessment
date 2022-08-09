# Write a program to find factors of a given number.
def factor(x, y):
    res = []
    for i in range(x, y):
        if y % i == 0:
            res.append(i)
    return res


num1 = int(input("Enter the number"))
num2 = int(input("Enter the number"))
result = factor(num1, num2)
print("factors are ", result)
