class Solution:
    def isPalindrome(self, s: str) -> bool:
        sanitStr = ''
        for i in s:
            if i.isalnum():
                sanitStr += i.lower()
                
        n = len(sanitStr)
        i = 0
        j = n - 1

        while i < j:
            if sanitStr[i] != sanitStr[j]:
                return False
            i += 1
            j -= 1
        return True
                
        