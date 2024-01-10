'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''


class Solution:

    # Function to find starting point where the truck can start to get through
    # the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        # Code here
        start = 0
        avail_pet = 0
        deficit = 0
        for i in range(n):
            avail_pet += (lis[i][0] - lis[i][1])
            if avail_pet < 0:
                deficit += avail_pet
                start = i + 1
                avail_pet = 0

        return start if (avail_pet + deficit) >= 0 else -1
