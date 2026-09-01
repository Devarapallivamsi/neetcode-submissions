class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        numset = set(nums)
        maxLen = 0
        for n in numset:
            if n - 1 not in numset:
                length = 1
                while n + length in numset:
                    length += 1
                maxLen = max(maxLen,length)
        return maxLen


                





