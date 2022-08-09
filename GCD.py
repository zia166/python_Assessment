# Find GCD of two numbers. GCD (Greatest Common Divisor) or HCF (Highest Common Factor) of two numbers is the largest number that divides both of them.


def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            total = i
    return total


num1 = int(input("Enter the number"))
num2 = int(input("Enter the second"))
result = hcf(num1, num2)
print("GCD of %s and %d is %s" % (num1, num2, result))
