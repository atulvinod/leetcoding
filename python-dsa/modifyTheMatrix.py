from typing import List

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        colMax = -float('inf')
        result = [row[:] for row in matrix]
        for col in range(len(matrix[0])):
            negativeNumberIndexes = []
            for row in range(len(matrix)):
                colMax = max(colMax, matrix[row][col])
                if result[row][col] == -1:
                    negativeNumberIndexes.append(row)
                
            for i in negativeNumberIndexes:
                result[i][col] = colMax
            colMax = -float('inf')
        
        return result

matrix = [[3,-1],[5,2]]
Solution().modifiedMatrix(matrix)