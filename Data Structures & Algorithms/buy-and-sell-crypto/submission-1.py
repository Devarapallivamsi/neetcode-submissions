import math
class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l,r = 0,1
        maxP = 0
        n = len(p)
        while r < n:
            if p[r] - p[l] > 0:
                maxP = max(maxP,p[r]-p[l])
            else:
                l = r
            r += 1
        return maxP
            



