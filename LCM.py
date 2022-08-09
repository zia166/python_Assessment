# Find the LCM of two numbers. LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers.


def compute_lcm(x, y):
    list_1 = [x, y]
    smaller = min(list_1)
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    lcm = (x * y) // hcf
    return lcm


num1 = int(input("enter the number"))
num2 = int(input("enter the number"))


print("LCM of number:", compute_lcm(num1, num2))
