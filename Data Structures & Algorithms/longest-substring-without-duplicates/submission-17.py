class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or s == '':
            return 0
        n = len(s)
        if n == 1:
            return 1
        # s = "zxyzxyz"
        # Non repeating substring.
        nonRepSubStr = set()
        maxLen = 0
        
        l = 0
        # r Starting from l itself makes sense coz, s[l] is where
        # we start looking at the substring.
        r = l
        while r < n:
            ch = s[r]
            # If the substring seen until now contains the current char,
            # keep greedily removing the chars starting from the left
            # until the nonRepSubStr upkeeps it's name (i.e., non repeating chars in the substring).
            while ch in nonRepSubStr:
                nonRepSubStr.remove(s[l])
                l += 1
            # After removing the duplicates, add the current char
            nonRepSubStr.add(ch)
            # Compute the max at every iteration. # Only this seems heavy
            maxLen = max(maxLen,r-l+1)
            r += 1
            
        return maxLen












                