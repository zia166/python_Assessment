# Write a program to find the sum of the digits of a given number?


def sum_of_digit(num):
    sum = 0
    while num != 0:
        x = num % 10
        sum = sum + x
        num = num // 10
    return sum


num = int(input("Enter the number"))
res = 0
res = sum_of_digit(num)
while res > 10:
    res = sum_of_digit(res)

else:
    print("sum of %s is %d " % (num, res))
