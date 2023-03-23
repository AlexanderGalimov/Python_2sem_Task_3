def read_two_dimensional_list(file):
    data = []
    with open(file) as f:
        for line in f:
            data.append([int(x) for x in line.split()])
    f.close()

    return data


def write_two_dimensional_list(data, max_square, file):
    f = open(file, 'w')
    for el in data:
        f.write(str(el.x) + " " + str(el.y) + "\n")

    f.write("\n")
    f.write(str(max_square))
    f.close()
