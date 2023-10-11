class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        n = len(image[0])
        for i in image:
            j = 0
            k = n - 1
            while j <= k:
                i[j], i[k] = i[k], i[j]
                i[j] ^= 1
                i[k] ^= 1
                if j == k:
                    i[j] ^= 1
                j += 1
                k -= 1
        return image
