def birthday(arr, d, m):
    r = 0

    for i in range(0, len(arr) - m + 1):
        c = 0

        for j in range(i, i + m):
            c += arr[j]

            if (c == d and j == i + m - 1):
                r += 1
                break

            if (c > d):
                break

    return r
