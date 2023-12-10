def swap(a1, a2, arr):
    while a1 < a2:
        arr[a1], arr[a2] = arr[a2], arr[a1]
        a1 += 1
        a2 -= 1


def rotate(arr, n):
    swap(n - 1, n - 1, arr)
    swap(0, n - 1 - 1, arr)
    swap(0, n - 1, arr)
    return arr



