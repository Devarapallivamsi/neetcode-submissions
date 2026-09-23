class MinStack:

    def __init__(self):
            self.stack = []
            self.mini = 2**31
            self.miniTracker = {}

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini = min(self.mini,val)
        self.miniTracker[len(self.stack)-1] = self.mini
        
    def pop(self) -> None:
        self.miniTracker.pop(len(self.stack)-1)
        self.stack.pop()
        if self.stack:
            self.mini = self.miniTracker[len(self.stack)-1]
        else:
            self.mini = 2**31
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.mini


        
