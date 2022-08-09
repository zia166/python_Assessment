# Write a program to find whether a number is prime or not. A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are {2, 3, 5, 7, 11, ….}

val = []
num = int(input("enter the number"))
flag = True
if num > 1:
    for i in range(2, num):

        if num % i == 0:
            pass

        else:
            val.append(i)


print("Prime numbers from 1 to %s are %s" % (num, val))
