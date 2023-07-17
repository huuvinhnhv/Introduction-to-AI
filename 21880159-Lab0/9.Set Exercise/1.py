# Exercise 6: Return a set of elements present
# in Set A or B, but not both
def solution(set1, set2):
    set3 = set()
    for i in set1:
        if i not in set2:
            set3.add(i)
    for i in set2:
        if i not in set1:
            set3.add(i)
    return set3


if __name__ == '__main__':
    set1 = {10, 20, 30, 40, 50}
    set2 = {30, 40, 50, 60, 70}
    set3 = solution(set1, set2)
    print(set3)
