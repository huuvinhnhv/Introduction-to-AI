def read_file(path):
    f = open(path, "r")
    data = f.readlines()
    f.close()
    return data


def write_file(path, data):
    f = open(path, "w")
    for i in range(0, len(data)):
        if i == 4:
            continue
        f.write(data[i])


if __name__ == '__main__':
    lines = read_file("test.txt")
    write_file("new_file.txt", lines)
