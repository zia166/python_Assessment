# Perfect numbers are the positive integers that are equal to the sum of its factors except for the number itself. Example: 6 is a perfect number, which is the sum of its proper divisors: 1, 2 and 3.
def perfect_number(n):
    res = []
    for i in range(1, n):
        if n % i == 0:
            res.append(i)
    if sum(res) == n:
        return True
    else:
        return False


num = int(input("Enter the number:"))
result = perfect_number(num)
if result == True:
    print("%s is perfect number" % num)
else:
    print("%s is not perfect number" % num)
