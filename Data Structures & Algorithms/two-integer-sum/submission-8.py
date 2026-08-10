class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSeen = {}

        for idx,val in enumerate(nums):
            diff = target-val
            if diff in prevSeen:
                return [prevSeen[diff],idx]
            prevSeen[val] = idx
        


       


        
        