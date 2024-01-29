class MyQueue:

    def __init__(self):
        self.main_stack = []
        self.temp_stack = []
        self.peekElement = None
        

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if self.peekElement is None:
            self.peekElement = x
        

    def pop(self) -> int:
        element = None
        
        while len(self.main_stack) != 0:
            self.temp_stack.append(self.main_stack.pop())
        element = self.temp_stack.pop()
        
        if len(self.temp_stack) != 0:
            self.peekElement = self.temp_stack[-1]
        else:
            self.peekElement = None
        
        while len(self.temp_stack) != 0:
            self.main_stack.append(self.temp_stack.pop())

        return element
        

    def peek(self) -> int:
        return self.peekElement
        

    def empty(self) -> bool:
        return len(self.main_stack) == 0
        
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

ops = ["MyQueue","push","pop","push","peek"]
args = [[],[1],[],[2],[]]

for i in range(len(ops)):
    if ops[i] == "MyQueue":
        obj = MyQueue()
    elif ops[i] == "push":
        print("push >", args[i][0])
        obj.push(args[i][0])
    elif ops[i] == "pop":
        print("pop >",obj.pop())
    elif ops[i] == "peek":
        print("peek > ",obj.peek())
    elif ops[i] == "empty":
        print("empty> ",obj.empty())