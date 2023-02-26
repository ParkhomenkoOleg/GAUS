import numpy as np
import sys


def calculation_from_file(path):
    with open(path, 'r') as f:
        a = [[float(num) for num in line.split(' ')] for line in f]

    num_of_lines = len(a)
    x = np.zeros(num_of_lines)

    for i in range(num_of_lines):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, num_of_lines):
            ratio = a[j][i] / a[i][i]

            for k in range(num_of_lines + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[num_of_lines - 1] = a[num_of_lines - 1][num_of_lines] / a[num_of_lines - 1][num_of_lines - 1]

    for i in range(num_of_lines - 2, -1, -1):
        x[i] = a[i][num_of_lines]

        for j in range(i + 1, num_of_lines):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    return x
