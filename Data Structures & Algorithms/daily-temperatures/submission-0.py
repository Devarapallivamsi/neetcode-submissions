class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n = len(temps)
        stacktemps = [] # Monotonically decreasing stack.
        res = [0]*n
        
        for currIdx,curTemp in enumerate(temps):
            while stacktemps and temps[stacktemps[-1]] < curTemp:
                stIdx = stacktemps.pop()
                res[stIdx] = currIdx - stIdx
            stacktemps.append(currIdx)
        return res
