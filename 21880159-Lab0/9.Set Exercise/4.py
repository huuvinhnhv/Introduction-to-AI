# Exercise 1: Add a list of elements to a set
# Given a Python list, Write a program to add
# all its elements into a given set.
def add_list_to_set(set1, list1):
    set1.update(list1)


if __name__ == '__main__':
    sample_set = {"Yellow", "Orange", "Black"}
    sample_list = ["Blue", "Green", "Red"]
    add_list_to_set(sample_set, sample_list)
    print(sample_set)
