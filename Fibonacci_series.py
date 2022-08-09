# Write a program to print the Fibonacci series up to n terms? Fibonacci series is a series of numbers where the current number is the sum of the previous two terms. For Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, ... , (n-1th + n-2th)
def fibonacci(num):
    total = [0, 1]
    for i in range(2, num + 1):
        total.append(total[i - 2] + total[i - 1])
    return total


res = []
num = int(input("Enter the number"))
res = fibonacci(num)
print(res)
