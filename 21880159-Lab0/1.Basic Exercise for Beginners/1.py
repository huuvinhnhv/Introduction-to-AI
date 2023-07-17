# Exercise 11: Write a Program to extract each
# digit from an integer in the reverse order.
def Nhap(note):
    value = eval(input(note))
    return value


def Solve(number):
    while number > 0:
        degit = number % 10
        number = number // 10
        print(degit, end=" ")


if __name__ == '__main__':
    n = Nhap("Nhap so can tinh: ")
    Solve(n)
