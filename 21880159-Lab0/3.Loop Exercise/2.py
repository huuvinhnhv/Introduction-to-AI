# Exercise 2: Print the following pattern
def Solve():
    for i in range(1, 6):
        for j in range(1, i + 1):
            print(j, end="")
        print()


if __name__ == '__main__':
    Solve()
