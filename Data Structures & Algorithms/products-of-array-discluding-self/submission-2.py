class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = 1
        res = [1]*n
        for i in range(n):
            res[i] = pref
            pref = pref*nums[i]
        
        post = 1
        for j in range(n-1,-1,-1):
            res[j] = res[j]*post
            post = post*nums[j]
        return res
            


        
            



        

