class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = {}
        for i in s:
            countS[i] = countS.get(i,0) + 1
        
        for j in t:
            if j in countS:
                countS[j] -= 1
            else:
                return False
        return set(countS.values()) == set([0])