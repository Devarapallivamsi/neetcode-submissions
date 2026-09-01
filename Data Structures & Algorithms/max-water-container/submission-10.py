class Solution:
    def maxArea(self, h: List[int]) -> int:
        maxA = 0
        if not h:
            return maxA
        
        n = len(h)
        i = 0
        j = n - 1
        while i < j:
            area = (j - i)*min(h[i],h[j])
            maxA = max(maxA,area)
            if h[i] < h[j]:
                i += 1
            else:
                j -= 1
        return maxA


