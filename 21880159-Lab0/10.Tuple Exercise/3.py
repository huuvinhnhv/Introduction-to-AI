# Exercise 10: Check if all items in the tuple are the same
def check_all_item(tup1):
    count = 0
    val = tup1[0]
    for i in tup1:
        if val == i:
            count += 1
    return count == len(tup1)


if __name__ == '__main__':
    tuple1 = (45, 45, 45, 45)
    print(check_all_item(tuple1))
