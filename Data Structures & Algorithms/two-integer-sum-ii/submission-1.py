class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hashValIdx = {}
        for idx,i in enumerate(nums):
            if target-i in hashValIdx:
                return [hashValIdx[target-i] + 1,idx+1]
            hashValIdx[i] = idx