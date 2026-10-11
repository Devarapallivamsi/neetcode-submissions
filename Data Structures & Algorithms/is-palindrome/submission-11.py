class Solution:
    def isPalindrome(self, s: str) -> bool:
        # CAPS-> 65 to 90
        # small -> 97 to 122
        # digits -> 48 to 57
        n = len(s)
        i = 0
        j = n -1
        while i < j:
            if not ((ord(s[i]) in range(65,91)) or 
                (ord(s[i]) in range(97,123)) or
                (ord(s[i]) in range(48,58))):
                i+= 1
                continue
            if not ((ord(s[j]) in range(65,91)) or
                (ord(s[j]) in range(97,123)) or
                (ord(s[j]) in range(48,58))):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True