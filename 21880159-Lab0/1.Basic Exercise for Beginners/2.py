# Exercise 12: Calculate income tax for
# the given income by adhering to the below rules
def Nhap(note):
    value = eval(input(note))
    return value


def Solve(income):
    tax = 0
    if income <= 10000:
        return tax
    elif income <= 20000:
        tax += (20000 - income) * 0.1
        return tax
    else:
        tax += 10000 * 0.1 + (income - 20000) * 0.2
        return tax


if __name__ == '__main__':
    n = Nhap("Nhap thu nhap cua ban: ")
    result = Solve(n)
    print(f"Tong thue la:{result}")
