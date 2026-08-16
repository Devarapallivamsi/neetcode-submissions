class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxSeqLength = 1
        nums = sorted(set(nums))
        n = len(nums)
        curr = 0
        i = 1
        while i < n:
            j = i
            seqLen = 1
            while j < n and (nums[j] == (nums[curr] + 1)):
                seqLen += 1
                if seqLen == n:
                    break
                curr = j
                j += 1

            maxSeqLength = max(maxSeqLength,seqLen)
            curr = j
            i = curr + 1
        return maxSeqLength
            






