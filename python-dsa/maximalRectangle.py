from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        currentHistogram = [0]* len(matrix[0])
        area = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                num = int(matrix[row][col])
                if num == 0:
                    currentHistogram[col] = 0
                else:
                    currentHistogram[col] += num
            currentMaxArea = self.histogramArea(currentHistogram)
            area = max(currentMaxArea, area)
        
        return area
        
        
    def histogramArea(self,numbers):
        stack = []
        previousLower = [-1 for _ in range(0, len(numbers))]
        nextLower = [len(numbers) for _ in range(0, len(numbers))]
        
        for i in range(0, len(numbers)):
            while len(stack) != 0  and numbers[stack[-1]] > numbers[i]:
                stack.pop()
            if len(stack) != 0:
                previousLower[i] = stack[-1]
            stack.append(i)
                
        stack.clear()
        for i in range(0, len(numbers)):
            while len(stack) != 0 and numbers[stack[-1]] > numbers[i]:
                greaterIndex = stack.pop()
                nextLower[greaterIndex] = i
            stack.append(i)
            
        area = 0
        for i in range(len(numbers)):
            cur = (nextLower[i] - previousLower[i] - 1)*numbers[i]
            area = max(area,cur)
        return area

matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Solution().maximalRectangle(matrix)