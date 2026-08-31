class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        scnt = {}
        tcnt = {}
        n = len(s)
        for i in range(n):
            scnt[s[i]] = scnt.get(s[i],0) + 1
            tcnt[t[i]] = tcnt.get(t[i],0) + 1
        return scnt == tcnt
        