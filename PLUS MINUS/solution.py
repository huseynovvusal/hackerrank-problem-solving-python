def plusMinus(arr):
    p = n = z = 0

    l = len(arr)

    for i in arr:
        if (i > 0):
            p += 1

        elif (i < 0):
            n += 1

        else:
            z += 1

    p = round(p / l, 6)
    n = round(n / l, 6)
    z = round(z / l, 6)

    print(p)
    print(n)
    print(z)
