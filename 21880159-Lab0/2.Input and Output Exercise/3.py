# Exercise 10: Read line number 4 from the following file
def read_file(path):
    f = open(path, "r")
    data = f.readlines()
    f.close()
    return data


def Nhap(note):
    n = eval(input(note))
    return n


if __name__ == '__main__':
    line_number = Nhap("Nhap dong muon doc: ")
    lines = read_file("test.txt")
    print(f"Dong {line_number} co du lieu la: \n {lines[line_number - 1]}", )
