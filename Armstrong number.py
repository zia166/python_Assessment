# Check the given number is Armstrong number or not. An Armstrong number is a number such that the sum of its digits raised to the number of digits is equal to the number itself.


def count(num):
    cnt = 0
    while num != 0:
        x = num % 10
        cnt = cnt + 1
        num = num // 10
    return cnt


num = num2 = int(input("Enter the number"))
cnt = count(num)


total = 0
for i in range(cnt):
    while num != 0:
        x = num % 10
        total = total + (x**cnt)
        num = num // 10
if total == num2:
    print("%s is amstrong number" % total)
else:
    print("%s is not amstrong number" % total)
