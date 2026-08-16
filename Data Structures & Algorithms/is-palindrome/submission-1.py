class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitStr = ''
        for i in s:
            if i.isalnum():
                try:
                    i = str(int(i))
                except:
                    i = i.lower()
                sanitStr += i
        n = len(sanitStr)
        i = 0
        j = n - 1

        while i < j:
            if sanitStr[i] != sanitStr[j]:
                return False
            i += 1
            j -= 1
        return True
                
        