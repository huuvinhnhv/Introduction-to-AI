# Exercise 5: Create a Python set such that it shows
# the element from both lists in a pair
def create_set_from_list(l1, l2):
    res_set = set()
    for i in range(len(l1)):
        res_set.add((l1[i], l2[i]))
    return res_set


if __name__ == '__main__':
    first_list = [2, 3, 4, 5, 6, 7, 8]
    second_list = [4, 9, 16, 25, 36, 49, 64]
    result = create_set_from_list(first_list, second_list)
    print("Final set:", result)
