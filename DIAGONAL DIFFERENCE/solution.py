def diagonalDifference(arr):
    d1 = 0
    d2 = 0

    n = len(arr)

    for i in range(0, n):
        d1 += arr[i][i]
        d2 += arr[i][n - i - 1]

    return abs(d1 - d2)
