# Exercise 6: Find the intersection (common) of two sets
# and remove those elements from the first set
def remove_intersection(s1, s2):
    intersection_set = set()
    for i in s1:
        if i in s2:
            intersection_set.add(i)
    print("Intersection is", intersection_set)
    for i in intersection_set:
        s1.remove(i)
    print("First Set after removing common element", s1)


if __name__ == '__main__':
    first_set = {23, 42, 65, 57, 78, 83, 29}
    second_set = {57, 83, 29, 67, 73, 43, 48}
    remove_intersection(first_set, second_set)
