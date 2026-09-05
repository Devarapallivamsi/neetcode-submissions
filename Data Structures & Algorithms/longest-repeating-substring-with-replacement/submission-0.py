class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '':
            return 0
        n = len(s)
        if n == 1:
            return 1
        l = 0
        ctr = {}
        maxF = 0
        maxLen = 0
        length = 0
        for r in range(n):
            ctr[s[r]] = ctr.get(s[r],0) + 1
            # print(ctr)
            maxF = max(ctr.values())

            # Window length - max repating elem in the window (seen till now) i.e., the other chars left <= k (num of replacements)
            if (r-l+1) - maxF <= k:
                length += 1
            else:
                ctr[s[l]] -= 1
                l += 1
            maxLen = max(maxLen,length)

        return maxLen

            




            
        



                
                    

