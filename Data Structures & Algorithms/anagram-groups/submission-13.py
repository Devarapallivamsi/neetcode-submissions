from typing import List
from collections import defaultdict

class Solution:
    # def isAnagram(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     countS = {}
    #     countT = {}
    #     for i in s:
    #         countS[i] = countS.get(i,0) + 1
    #     for j in t:
    #         countT[j] = countT.get(j,0) + 1
        
    #     return countS == countT

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for strng in strs:
            count = [0]*26
            for ch in strng:
                count[ord(ch)-ord('a')] += 1
            anagrams[tuple(count)].append(strng)
        return list(anagrams.values())
        











