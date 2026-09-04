class Solution:
    def trap(self, h: List[int]) -> int:
        lmax = 0
        rmax = 0
        n = len(h)

        lmaxArr = [None]*n
        rmaxArr = [None]*n
        for i in range(n):
            lmaxArr[i] = lmax
            rmaxArr[n-i-1] = rmax
            lmax = max(lmax,h[i])
            rmax = max(rmax,h[n-i-1])
        # print(lmaxArr)
        # print(rmaxArr)
        
        water = 0
        for j in range(n):
            # Get the min height between the maximums of left and right.
            # Subtract it with current height h[j] to get the height wise dimension
            # Across the length, it is always 1 coz, we are calculating the area
            # of water that can be stored at each bar.
            height = min(lmaxArr[j],rmaxArr[j]) - h[j]
            if height > 0:
                water += height
            
        return water

