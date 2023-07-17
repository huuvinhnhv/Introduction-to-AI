# Exercise 15: Write a function called exponent(base, exp)
# that returns an int value of base raises to the power of exp.
def Nhap(note):
    value = eval(input(note))
    return value


def Solve(base, exponent):
    result = 1
    num = exponent
    while num > 0:
        result *= base
        num -= 1
    return result


if __name__ == '__main__':
    b = Nhap("Nhap base: ")
    e = Nhap("Nhap exponent: ")
    n = Solve(b, e)
    print(f"{b} luy thua {e} = {n}.")
