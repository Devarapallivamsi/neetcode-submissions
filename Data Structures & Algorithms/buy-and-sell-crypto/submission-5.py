import math
class Solution:
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        r = 1
        n = len(p)
        maxP = 0
        while l < r and r < n:
            if p[r]-p[l] < 0:
                l = r
                r+= 1
            else:
                maxP = max(maxP,p[r]-p[l])
                r+=1
        return maxP