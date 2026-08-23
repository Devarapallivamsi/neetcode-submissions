class Solution:
    def trap(self, h: List[int]) -> int:
        area = 0
        n = len(h)
        LmaxArr = [None]*n
        RmaxArr = [None]*n
        lmax = 0
        rmax = 0
        
        LmaxArr[0] = lmax
        RmaxArr[n-1] = rmax
        for i in range(1, n - 1):
            
            lmax = max(lmax,h[i-1])
            LmaxArr[i] = lmax

            rmax = max(rmax,h[(n-i-1)+1])
            RmaxArr[n-i-1] = rmax
        LmaxArr[n-1] = lmax
        RmaxArr[0] = rmax

        for i in range(n):
            curArea = min(LmaxArr[i],RmaxArr[i]) - h[i]
            if curArea >= 0:
                area += curArea
        return area
       