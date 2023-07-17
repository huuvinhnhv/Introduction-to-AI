# Exercise 5: Accept a list of 5 float numbers as an input from the user
def Nhap(note):
    print(note)
    numbers = []
    for i in range(0, 5):
        print(f"Nhap phan thu thu [{i}]: ")
        value = float(input())
        numbers.append(value)
    return numbers


def Xuat(arr):
    print("List: ", arr)


if __name__ == '__main__':
    nums = Nhap("Nhap mang so thuc:")
    Xuat(nums)
