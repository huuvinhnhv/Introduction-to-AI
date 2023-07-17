# Exercise 2: Create a function with variable
# length of arguments

def func1(*params):
    print("Params: ")
    for i in params:
        print(i, end=" ")


if __name__ == '__main__':
    func1(20, 40, 60)
    print()
    func1(80, 100)
