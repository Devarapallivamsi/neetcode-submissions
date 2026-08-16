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
        return sanitStr == sanitStr[::-1]
                
        