from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        functions = {
            "+" : lambda x,y:x+y,
            "-": lambda x,y:y-x,
            "*": lambda x,y:x*y,
            "/":lambda x,y:int(y/x)
        }
        operations = set(functions.keys())
        for t in tokens:
            if t in operations:
                a = stack.pop()
                b = stack.pop()
                result = functions[t](a,b)
                stack.append(result)
            else:
                stack.append(int(t))
                
        return stack.pop()

print(Solution().evalRPN( ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
                