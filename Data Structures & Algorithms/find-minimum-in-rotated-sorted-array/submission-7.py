class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        if nums[0] <= nums[-1]:
            return nums[0]
        
        l = 0
        r = n - 1
        mini = float("infinity")
        while l <= r:
            mid = (l + r) // 2
            # This mini variable is being used to consider nums[mid] as well.
            # coz, this will be skipped due to mid + 1 and mid - 1 in the iteration.
            mini = min(mini, nums[mid])
            # if l == r:
            #     return mini

            # If the middle element is less than the last element.
            # mid belongs to the right half (in the sorted array).
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid - 1
        return mini
            
                


