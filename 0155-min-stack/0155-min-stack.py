class MinStack:

    def __init__(self):
        self.stk = []
        self.minStk=  []        

    def push(self, val: int) -> None:
        self.stk.append(val)

        if not self.minStk:
            self.minStk.append(val)
        elif self.minStk[-1] < val:
            self.minStk.append(self.minStk[-1])
        else:
            self.minStk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minStk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()