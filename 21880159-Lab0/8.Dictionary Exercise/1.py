# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program
# to convert them into a dictionary in a way that
# item from list1 is the key and item from list2 is
# the value
def convert_list_to_dict(key, val):
    set2 = set()
    for i in range(len(key)):
        set2.add((key[i], val[i]))
    return dict(set2)


if __name__ == '__main__':
    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]
    dict1 = convert_list_to_dict(keys, values)
    print(dict1)
