class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefMul = [None]*n
        sufMul = [None]*n
        preProd = 1
        sufProd = 1 
        for i in range(n):
            prefMul[i] = preProd*nums[i]
            preProd = preProd*nums[i]
            sufMul[n-i-1] = sufProd*nums[n-i-1]
            sufProd = sufProd*nums[n-i-1]
        output = [None]*n
        
        for j in range(n):
            preMul = nextMul = None
            if j == 0:
                preMul = 1
                nextMul = sufMul[j+1]
            elif j == n-1:
                preMul = prefMul[j-1]
                nextMul = 1
                
            else:
                preMul = prefMul[j-1]
                nextMul = sufMul[j+1]
            output[j] = preMul * nextMul
        return output

            



        

