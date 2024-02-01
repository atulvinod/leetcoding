from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        nextGreater = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            while len(stack) != 0 and temperatures[i] > temperatures[stack[-1]]:
                topElement = stack.pop()
                nextGreater[topElement] = i - topElement
            stack.append(i)

        return nextGreater

Solution().dailyTemperatures([73,74,75,71,69,72,76,73])        