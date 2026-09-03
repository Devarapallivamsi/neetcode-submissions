class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or s == '':
            return 0
        # s = "zxyzxyz"
        # Non repeating substring.
        nonRepSubStr = set()
        maxLen = 0
        n = len(s) # 7
        l = 0
        r = l
        while r < n:
            ch = s[r]
            while ch in nonRepSubStr:
                nonRepSubStr.remove(s[l])
                l += 1
            nonRepSubStr.add(ch)
            maxLen = max(maxLen,r-l+1)
            r += 1
            
        return maxLen












                