def miniMaxSum(arr):
    arr = sorted(arr)

    s = sum(arr)

    print(s - arr[len(arr) - 1], s - arr[0])
