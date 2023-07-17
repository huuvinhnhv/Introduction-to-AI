# Exercise 2: Return a new set of identical
# items from two sets
def create_identical_set(set1, set2):
    set3 = set()
    for i in set1:
        if i in set2:
            set3.add(i)
    return set3


if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = create_identical_set(set1, set2)
    print(set3)
