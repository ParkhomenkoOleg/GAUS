from solver import solve


def calculation_from_file(path):
    with open(path, 'r') as f:
        a = [[float(num) for num in line.split(' ')] for line in f]

    result = solve(a)
    return result
