import numpy as np
import sys


def conversion_from_str(pre_result):
    for i in range(len(pre_result)):
        for j in range(len(pre_result[i])):
            pre_result[i][j] = float(pre_result[i][j])
    return pre_result


def solve(pre_result):
    a = conversion_from_str(pre_result)

    # Reading number of unknowns
    size = len(a)

    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(size)

    # Applying Gauss Elimination
    for i in range(size):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')
        for j in range(i + 1, size):
            ratio = a[j][i] / a[i][i]
            for k in range(size + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[size - 1] = a[size - 1][size] / a[size - 1][size - 1]

    for i in range(size - 2, -1, -1):
        x[i] = a[i][size]
        for j in range(i + 1, size):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution
    temp_str = ""
    for i in range(size):
        temp_str += "x{}  = {}\n".format(i, (round(x[i], 2)))

    return temp_str


# 4,42	12,6	5,77	1,56
# 0,16	3,82	6,41	4,42
# 7,14	4,98	8,73	-2,67
if __name__ == '__main__':
    print("data", solve([['2', '7', '3', '980'], ['3', '4', '5', '780'], ['5', '6', '1', '860']]))
