# Importing NumPy Library
import numpy as np
import sys


def solve(pre_result):
    for i in range(len(pre_result)):
        for j in range(len(pre_result[i])):
            pre_result[i][j] = float(pre_result[i][j])
    matrix = pre_result
    # Reading number of unknowns
    n = 3

    # Making numpy array of n x n+1 size and initializing
    # to zero for storing augmented matrix
    a = matrix
    # a = np.zeros((n, n + 1))

    # Making numpy array of n size and initializing
    # to zero for storing solution vector
    x = np.zeros(n)

    # Reading augmented matrix coefficients
    # print('Enter Augmented Matrix Coefficients:')
    # for i in range(n):
    #     for j in range(n + 1):
    #         a[i][j] = float(input('a[' + str(i) + '][' + str(j) + ']='))

    # Applying Gauss Elimination
    for i in range(n):
        if a[i][i] == 0.0:
            sys.exit('Divide by zero detected!')

        for j in range(i + 1, n):
            ratio = a[j][i] / a[i][i]

            for k in range(n + 1):
                a[j][k] = a[j][k] - ratio * a[i][k]

    # Back Substitution
    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = a[i][n]

        for j in range(i + 1, n):
            x[i] = x[i] - a[i][j] * x[j]

        x[i] = x[i] / a[i][i]

    # Displaying solution
    # print('\nRequired solution is: ')
    str = ""
    for i in range(n):
        temp_str = "{} ".format(round(x[i]))
        # str += str.format('X%d = %0.2f\n', )
        str += temp_str

    return str
    # print('X%d = %0.2f' % (i, x[i]), end='\t')


# 4,42	12,6	5,77	1,56
# 0,16	3,82	6,41	4,42
# 7,14	4,98	8,73	-2,67
if __name__ == '__main__':
    print("data", solve([['2', '7', '3', '980'], ['3', '4', '5', '780'], ['5', '6', '1', '860']]))
