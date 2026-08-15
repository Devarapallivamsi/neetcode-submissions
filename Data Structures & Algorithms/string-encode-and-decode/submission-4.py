class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for s in strs:
            length = len(s)
            encodedStr += str(length) + '#' + s
        print(encodedStr)
        return encodedStr


    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        words = []
        while i < n:
            j = i + 1
            while s[j] != '#':
                j += 1
            wordLen = int(s[i:j])
            word = s[j+1:j+wordLen+1]
            words.append(word)
            i = j + wordLen + 1
        return words



        
