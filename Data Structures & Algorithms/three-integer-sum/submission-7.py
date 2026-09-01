class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        res = set()
        i = 0
        n = len(nums)
        while i < n:
            j = i + 1
            k = n - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    ele = (nums[i],nums[j],nums[k])
                    if ele not in res:
                        res.add(ele)
                    j += 1
                elif _sum < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        
        return [list(ele) for ele in res]
                
            