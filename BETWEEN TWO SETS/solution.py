def getTotalX(arr1, arr2):
    result = 0

    start = max(arr1)
    end = min(arr2)

    for i in range(start, end + 1):
        isDivisibleA = True
        isDivisibleB = True

        for a in arr1:
            if (i % a != 0):
                isDivisibleA = False
                break

        for b in arr2:
            if (b % i != 0):
                isDivisibleB = False
                break

        if (isDivisibleA and isDivisibleB):
            result += 1

    return result
