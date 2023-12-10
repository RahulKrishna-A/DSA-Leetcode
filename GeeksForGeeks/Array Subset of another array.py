# User function Template for python3

def isSubset(a1, a2, n, m):
    hash1 = {}
    for i in a1:
        if i in hash1:
            hash1[i] += 1
        else:
            hash1[i] = 1
    for i in a2:
        if i in hash1:
            if hash1[i] > 0:
                hash1[i] -= 1
                continue

        return "No"
    return "Yes"
