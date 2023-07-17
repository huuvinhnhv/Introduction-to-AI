# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age).
# Assign a new name show_student(name, age) to it and call it using the new name.
def display_student(name, age):
    print(name, age)


def show_student(name, age):
    return display_student(name, age)


if __name__ == '__main__':
    show_student("Vinh", 29)
