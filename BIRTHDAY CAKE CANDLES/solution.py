def birthdayCakeCandles(candles):
    maximum = candles[0]

    count = 0

    for candle in candles:
        if (candle == maximum):
            count += 1

        if (candle > maximum):
            maximum = candle
            count = 1

    return count
