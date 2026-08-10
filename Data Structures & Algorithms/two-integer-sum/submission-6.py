class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsIdx = [[val,idx] for idx,val in enumerate(nums)]

        numsIdxSortednums = sorted(numsIdx,key = lambda nestedList: nestedList[0])
        
        i = 0
        j = len(numsIdxSortednums) - 1
        while i < j:
            # accessing values
            _sum = numsIdxSortednums[i][0] + numsIdxSortednums[j][0]
            if _sum == target:
                return [min(numsIdxSortednums[i][1],numsIdxSortednums[j][1]),
                        max(numsIdxSortednums[i][1],numsIdxSortednums[j][1])]
            elif _sum < target:
                i += 1
            else:
                j -= 1

       


        
        