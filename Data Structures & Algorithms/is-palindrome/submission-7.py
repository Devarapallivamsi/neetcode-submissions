class Solution:
    def isPalindrome(self, s: str) -> bool:
        alNumsStr = ''.join([c.lower() for c in s if c.isalnum()])
        n = len(alNumsStr)
        i = 0
        j = n - 1
        while i < j:
            if alNumsStr[i] != alNumsStr[j]:
                return False
            i += 1
            j -= 1
        return True
        