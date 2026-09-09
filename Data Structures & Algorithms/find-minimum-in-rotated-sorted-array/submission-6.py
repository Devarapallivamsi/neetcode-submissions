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
            if nums[l] <= nums[r]:
                return min(mini,nums[l])
            
            mid = (l + r) // 2
            mini = min(mini,nums[mid])
            # When we are in the right half portion before the pivot
            # [1,2,3,4,5,6]
            # [3,4,5,6,1,2] (rotated by 4 positions)
            # so, right half before pivot is [3,4,5,6]
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid -  1
        return mini



                


