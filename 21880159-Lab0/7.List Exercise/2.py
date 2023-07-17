# Exercise 4: Concatenate two lists in the following order
def concatenate_tow_list(l1, l2):
    l3 = []
    for i in l1:
        for j in l2:
            l3.append(i + j)
    return l3


if __name__ == '__main__':
    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    result = concatenate_tow_list(list1, list2)
    print(result)
