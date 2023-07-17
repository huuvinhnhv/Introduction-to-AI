# Exercise 8: Update set1 by adding items from set2,\
# except common items
def update_set(set1, set2):
    set3 = set()
    for i in set1:
        if i not in set2:
            set3.add(i)
    for i in set2:
        if i not in set1:
            set3.add(i)
    set1.clear()
    set1.update(set3)


if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    update_set(set1, set2)
    print(set1)
