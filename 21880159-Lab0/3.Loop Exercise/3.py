# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in
# a number using a while loop.
# For example, the number is 75869, so the output should be 5.
def input_value(note):
    n = eval(input(note))
    return n


def solve(num):
    count = 0
    n = num
    while n != 0:
        n = n // 10
        count += 1
    return count


if __name__ == '__main__':
    number = input_value("Nhap mot so nguyen duong: ")
    result = solve(number)
    print(f"So luong chu so cua {number}: {result}")
