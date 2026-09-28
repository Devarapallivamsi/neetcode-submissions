class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1

        n = len(s)
        maxLen = 0
        w = set()
        l = 0
        for r in range(n):
            while s[r] in w:
                w.remove(s[l])
                l += 1
            maxLen = max(maxLen,r-l+1)
            w.add(s[r])
            
        return maxLen

            












                