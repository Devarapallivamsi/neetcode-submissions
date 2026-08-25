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
        r = 0

        while r < n:
            if s[r] in w:
                maxLen = max(maxLen, len(w))
                # ssl is 'substring left'
                ssl = l
                while s[r] in w:
                    w.remove(s[ssl])
                    ssl += 1
                l = ssl
            w.add(s[r])
            r += 1
        return max(maxLen,len(w))

            












                