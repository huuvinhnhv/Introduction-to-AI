# Exercise 13: Print multiplication table form 1 to 10
def Solve():
    for i in range(1, 11):
        for j in range(1, 11):
            print(i * j, end=" ")
        print("\t\t")


if __name__ == '__main__':
    Solve()
