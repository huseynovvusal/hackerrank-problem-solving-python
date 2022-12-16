def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(0, 3):
        if (a[i] > b[i]):
            alice += 1
        if (a[i] < b[i]):
            bob += 1

    return [alice, bob]
