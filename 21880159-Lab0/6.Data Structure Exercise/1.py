# Exercise 1: Create a list by picking an
# odd-index items from the first list and
# even index items from the second
# Given two lists, l1 and l2, write a program
# to create a third list l3 by picking an odd-index
# element from the list l1 and even index elements
# from the list l2.
def create_list(l1, l2):
    odd_index = []
    for i in range(len(l1)):
        if i % 2 != 0:
            odd_index.append(l1[i])
    even_index = []
    for i in range(len(l2)):
        if i % 2 == 0:
            even_index.append(l2[i])
    print("Odd-index: ")
    print(odd_index)
    print("Even-index: ")
    print(even_index)
    print("Final list:")
    final_list = odd_index + even_index
    print(final_list)


if __name__ == '__main__':
    l1 = [3, 6, 9, 12, 15, 18, 21]
    l2 = [4, 8, 12, 16, 20, 24, 28]
    create_list(l1, l2)
