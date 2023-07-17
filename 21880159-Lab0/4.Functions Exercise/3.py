# Exercise 3: Return multiple values from a function
# Write a program to create function calculation()
# such that it can accept two variables and calculate
# addition and subtraction. Also, it must return both
# addition and subtraction in a single return call.
def input_value():
    a = int(input("Nhap a: "))
    b = int(input("Nhap b: "))
    return a, b


def calculation(a, b):
    return a + b, a - b


if __name__ == '__main__':
    a, b = input_value()
    res = calculation(a, b)
    print(res)
