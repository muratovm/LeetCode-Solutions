class MyQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, x: int) -> None:
        if len(self.stack_1) == 0:
            self.stack_2.append(x)
        else:
            self.stack_1.append(x)        

    def pop(self) -> int:
        if self.empty(): return None
        
        if len(self.stack_1) != 0:
            element = self.stack_1[0]
            self.stack_2 = self.stack_1[1:]
            self.stack_1 = []
        elif len(self.stack_2) != 0:
            element = self.stack_2[0]
            self.stack_1 = self.stack_2[1:]
            self.stack_2 = []
        else:
            return None
        return element
            
    def peek(self) -> int:
        if self.empty(): return None
        
        if not len(self.stack_1) == 0:
            return self.stack_1[0]
        if not len(self.stack_2) == 0:
            return self.stack_2[0]
        

    def empty(self) -> bool:
        return len(self.stack_1) + len(self.stack_2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
