from collections import deque
import operator as o
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        ops = {"+":o.add, "-":o.sub, "*":o.mul, "/":lambda x,y:int(x/y)}
        # res = 0
        for i in tokens:
            if i in ops:
                a = stack.pop() # 5
                b = stack.pop() # 13
                res = ops[i](int(b), int(a))
                stack.append(str(res))
            else:
                stack.append(i)
            
        return int(stack[-1])
        