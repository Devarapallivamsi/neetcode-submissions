class Solution:
    def isPalindrome(self, s: str) -> bool:
        alNums = [c.lower() for c in s if c.isalnum()]
        alNumsStr = ''.join(alNums)
        n = len(alNumsStr)
        i = 0
        j = n - 1
        while i < j:
            if alNumsStr[i] != alNumsStr[j]:
                return False
            i += 1
            j -= 1
        return True
        