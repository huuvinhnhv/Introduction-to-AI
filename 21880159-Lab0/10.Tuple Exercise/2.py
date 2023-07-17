# Exercise 6: Copy specific elements from one
# tuple to a new tuple
# Write a program to copy elements 44 and 55 from
# the following tuple into a new tuple.
if __name__ == '__main__':
    tuple1 = (11, 22, 33, 44, 55, 66)
    set1 = set()
    for i in tuple1:
        if i == 44 or i == 55:
            set1.add(i)
    tuple2 = tuple(set1)
    print(tuple2)
