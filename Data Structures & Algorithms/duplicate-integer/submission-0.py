class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupTracker = {}
        for i in nums:
            if i in dupTracker:
                return True
            dupTracker[i]=1
        return False