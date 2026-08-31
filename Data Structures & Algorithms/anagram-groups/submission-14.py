from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        charsCountTupleTo_Words = defaultdict(list)
        for s in strs:
            charsCount = [0]*26 # As each string is composed of only lower case english alphabets; idx 0 represents the count of chars 'a' in the s; Similarly, idx 1 --> count of chars 'b' in s. likewise follows;
            for c in s:
                # ord(c)-ord('a') --> This would normalize the number to be in range [0,25]; 0 == 'a'; 1 == 'b'
                # ord(c) --> ASCII value of current char.
                charsCount[ord(c)-ord('a')] += 1
            charsCountTupleTo_Words[tuple(charsCount)].append(s)
        return list(charsCountTupleTo_Words.values())




