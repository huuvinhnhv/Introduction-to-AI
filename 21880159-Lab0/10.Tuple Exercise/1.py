# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a
# Python program to print the value 20.

if __name__ == '__main__':
    tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
    val = tuple1[1][1]
    print(val)
