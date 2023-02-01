def breakingRecords(scores):
    best = scores[0]
    worst = scores[0]

    b_count = w_count = 0

    for i in scores:
        if (i > best):
            best = i
            b_count += 1

        if (i < worst):
            worst = i
            w_count += 1

    return [b_count, w_count]
