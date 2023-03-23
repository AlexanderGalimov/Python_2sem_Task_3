import itertools

import file_permutations


class Point:
    coordinates = []

    def __init__(self, cur_x, cur_y):
        self.x = cur_x
        self.y = cur_y
        self.coordinates = [cur_x, cur_y]


def remove_same_rows(source_matrix):
    points = []

    for el in source_matrix:
        if el not in points:
            p = Point(el[0], el[1])
            points.append(p)

    return points


def count_square(data):
    under_abs = (data[1].x - data[0].x) * (data[2].y - data[0].y) - (data[2].x - data[0].x) * (
            data[1].y - data[0].y)

    return 0.5 * abs(under_abs)


def form_permutations(points):
    curr = list(itertools.combinations(remove_same_rows(points), 3))

    return curr


def find_max_square(data):
    maximum = -1
    max_el = []
    for el in data:
        curr_s = count_square(el)
        if curr_s > maximum:
            maximum = curr_s
            max_el = el

    return max_el, maximum


def run_program(input_path, output_path):
    points = file_permutations.read_two_dimensional_list(input_path)

    result, max_square = find_max_square(form_permutations(points))

    file_permutations.write_two_dimensional_list(result, max_square, output_path)


def print_matrix(src):
    for i in range(len(src)):
        for j in range(len(src[0])):
            print(str(src[i][j]) + " ", end="")
        print()


def print_points(src):
    for el in src:
        print(str(el.x) + " " + str(el.y))

