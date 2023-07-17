# Exercise 1: Create a function in Python
# Write a program to create a function that
# takes two arguments, name and age, and print their value.
def input_info():
    name = input("Nhap ten: ")
    age = int(input("Nhap tuoi: "))
    return name, age


def show_info(name, age):
    print(f"Name: {name}\nAge: {age}")


if __name__ == '__main__':
    # show_info("Vinh", 29)
    name, age = input_info()
    show_info(name, age)
