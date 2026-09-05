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
            # For each char, keep a track of it's frequency
            ctr[s[r]] = ctr.get(s[r],0) + 1
            # Find the max frequency -- most occured element until now.
            maxF = max(maxF, ctr[s[r]])

            # Window length - (minus) max repating elem in the window (seen till now) i.e., the other chars left <= k (num of replacements) ==> This means, we can make this window to have same character throughout.
            if (r-l+1) - maxF <= k:
                length += 1
            else:
                # Decrement the counter of s[l] by one in the freq ctr hashmap (dictionary)
                ctr[s[l]] -= 1
                l += 1
            # This is done at every iteration coz, the iter may go into if or else.
            maxLen = max(maxLen,length)

        return maxLen

            




            
        



                
                    

