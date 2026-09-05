class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1ctr = {}
        for i in s1:
            s1ctr[i] = s1ctr.get(i,0) + 1

        def isAnagram(s1dict,sstr2):
            s2dict = {}
            for j in sstr2:
                s2dict[j] = s2dict.get(j,0) + 1
            return s1dict == s2dict

        k = len(s1)
        n = len(s2)
        for i in range(n-k+1):
            substr = s2[i:i+k]
            if isAnagram(s1ctr,substr):
                return True
        return False
            


        
        
        
        
        


