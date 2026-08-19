class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0 
        if not heights:
            return maxArea
        n = len(heights)

        i = 0
        j = n - 1
        
        while i < j:
            leftH = heights[i]
            rightH = heights[j]
            maxArea = max(maxArea, min(leftH,rightH)*(j-i))
            # This condition is crucial. As in, when the pointer is moved, we are decreasing the length between the pointers. so, we should aim to move the pointer which has the potential to increase the min height -- which would in turn increase the area.
            if leftH < rightH:
                i += 1
            else:
                j -= 1
        return maxArea