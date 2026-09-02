import math
class Solution:
    # Best Time to Buy and Sell Stock
    def maxProfit(self, p: List[int]) -> int:
        l = 0
        r = 1
        n = len(p)
        maxP = 0
                        # Ensure right pointer does not
                        # cross bounds of the array (days)
        while l < r and r < n:
            # If profit is less, move the left pointer all the way to the
            # right pointer and make the right pointer move one step fwd.
            # Why? Consider [7, 8, 10, 3, 9, 6]
            # when l is at 7 and r is at 10, the max profit recorded is 3 (10-7). 
            # (but 8 - 3 is 5 or 10 - 3 is 7 -- even more profit? Nope.
            # Only move forward and make the profit computation 
            # as (future day price - current day price)
            # not the other way around.
            # next, the moment r is at 3, the profit is 3 - 7 = -4 (loss)
            # so, I will move to the new loss making day (l) and seek
            # for that day that might give me a better profit from there on.
            # Simply put, r moves forward blindly. but l moves only when it sees
            # loss in the hindsight.

            if p[r]-p[l] <= 0:
                l = r
            else:
                maxP = max(maxP,p[r]-p[l])
            # r has no cognisance of the l and just keeps moving.
            r+=1
        return maxP