class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        res = ''
        for s in strs:
            res += str(len(s))+'#'+s
        return res


    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        n = len(s)
        i = 0
        print(s)
        res = []
        while i < n:
            num = ''
            j = i
            while s[j] != '#':
                num += s[j]
                j += 1
            print(num)
            
            numint = int(num)
            i = j + numint + 1
            word = s[j+1:j+numint+1]
            res.append(word)
        
        return res



        