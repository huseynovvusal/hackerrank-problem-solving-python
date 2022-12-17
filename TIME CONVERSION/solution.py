def setClock(h, m, s):

    if (h < 10):
        h = "0" + str(h)

    if (h == 24):
        h = "00"

    return f"{h}:{m}:{s}"


def timeConversion(s):
    part = s[-2:]
    hour = int(s[0:2])
    minute = s[3:5]
    second = s[6:8]

    clock = setClock(hour, minute, second)

    if (part == "PM"):
        if (hour < 12):
            hour += 12
            clock = setClock(hour, minute, second)
    else:
        if (hour >= 12):
            hour -= 12
            clock = setClock(hour, minute, second)

    return clock
