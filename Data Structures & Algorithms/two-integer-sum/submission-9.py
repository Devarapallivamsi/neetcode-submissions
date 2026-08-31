class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx,val in enumerate(nums):
            reqd = target-val
            if reqd in seen:
                return [seen[reqd],idx]
            seen[val] = idx
            # print(seen)