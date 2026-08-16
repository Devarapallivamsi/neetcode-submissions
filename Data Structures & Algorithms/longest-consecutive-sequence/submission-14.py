import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeqLen = 0
        for n in numSet:
            # This means we found a num that can be present at the beginning of a sequence
            if n - 1 not in numSet:
                length = 1
                while n + length in numSet:
                    length += 1
                maxSeqLen = max(maxSeqLen,length)
        return maxSeqLen
        


        