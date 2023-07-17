# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an
# input string’s first, middle, and last character.

def input_string():
    return input("Nhap chuoi: ")


def create_string(str):
    first = 0
    mid = len(str) // 2
    last = len(str) - 1
    return str[first] + str[mid] + str[last]


if __name__ == '__main__':
    old_str = input_string()
    new_str = create_string(old_str)
    print(new_str)
