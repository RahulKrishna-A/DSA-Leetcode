def hasArrayTwoCandidates( arr, n, x):
    # code here
    hashs = {}
    for i in range(n):
        if x - arr[i] in hashs:

            return 1

        if arr[i] not in hashs:
            hashs[arr[i]] = i
    return 0

print(hasArrayTwoCandidates([335, 501, 170, 725, 479, 359, 963, 465, 706, 146, 282, 828, 962, 492, 996, 943, 828, 437, 392, 605, 903, 154, 293, 383, 422, 717, 719, 896, 448, 727, 772, 539, 870, 913, 668, 300, 36, 895, 704, 812, 323, 334],2,468))