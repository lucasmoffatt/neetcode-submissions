class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.minstack:
            self.minstack.append(val)
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
        elif val > self.minstack[-1]:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        del self.stack[-1]
        del self.minstack[-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
