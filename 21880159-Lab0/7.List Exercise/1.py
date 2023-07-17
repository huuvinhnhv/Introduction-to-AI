# Exercise 1: Reverse a list in Python
def reverse_list(l):
    l2 = l[::-1]
    return l2


if __name__ == '__main__':
    list1 = [100, 200, 300, 400, 500]
    result = reverse_list(list1)
    print(result)
