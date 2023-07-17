# Exercise 3: Calculate the sum of all numbers
# from 1 to a given number
def input_value():
    return int(input("Nhap mot so nguyen duong: "))


def sum_calculation(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


if __name__ == '__main__':
    n = input_value()
    sum = sum_calculation(n)
    print("Sum: ", sum)
