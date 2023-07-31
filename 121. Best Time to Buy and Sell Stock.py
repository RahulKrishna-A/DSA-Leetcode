class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mins = prices[0]
        pro = 0
        for i in prices:
            if i < mins:
                mins = i
            if i - mins > pro:
                pro = i - mins
        return pro



