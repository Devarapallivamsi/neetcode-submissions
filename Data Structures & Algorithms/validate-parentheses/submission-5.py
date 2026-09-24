class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        mystack = []
        match = {'}':'{',']':'[',')':'('}
        for i in s:
            if i in {'[','(','{'}:
                mystack.append(i)
            else:
                if len(mystack) == 0 or match[i] != mystack.pop():
                    return False
                
        return len(mystack) == 0
        