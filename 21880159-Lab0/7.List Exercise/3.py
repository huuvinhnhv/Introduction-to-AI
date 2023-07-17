# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove
# all occurrences of item 20.
def remove_all(list2, value):
    while True:
        list2.remove(value)
        if value not in list2:
            break


if __name__ == '__main__':
    list1 = [5, 10, 15, 20, 25, 50, 20]
    remove_all(list1, 20)
    print(list1)
