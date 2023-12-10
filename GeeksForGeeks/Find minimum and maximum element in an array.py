def getMinMax(a, n):
    mins = a[0]
    maxs = a[0]
    for i in a:
        if i > maxs:
            maxs = i
        if mins > i:
            mins = i
    return [mins, maxs]
