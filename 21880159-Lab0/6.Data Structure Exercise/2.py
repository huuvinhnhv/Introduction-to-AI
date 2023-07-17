# Exercise 2: Remove and add item in a list
# Write a program to remove the item present
# at index 4 and add it to the 2nd position and
# at the end of the list.
def remove_and_add(l1):
    temp = l1[4]
    l1.pop(4)
    print("List after remove at index 4 ", l1)
    l1.insert(2, temp)
    print("List after insert at index 2 ", l1)
    l1.append(temp)
    print("List after append at the last index ", l1)
    l1.append(temp)


if __name__ == '__main__':
    sample_list = [34, 54, 67, 89, 11, 43, 94]
    remove_and_add(sample_list)
