class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myStack = []
        for p,s in sorted(zip(position,speed)):
            t = (target - p)/s
            # print(t)
            myStack.append(t)
        
        

        fleet = 1
        n = len(myStack)
        cur = myStack.pop()
        while myStack:
            new = myStack.pop()
            if new <= cur:
                pass
            else:
                fleet += 1
                cur = new
        return fleet

        

        