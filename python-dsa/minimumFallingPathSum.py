from typing import List
'''
https://leetcode.com/problems/minimum-falling-path-sum
'''

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = dict()
        def inBounds(x,y):
            return x < len(matrix) and x >= 0 and y < len(matrix[0]) and y >= 0
        
        def pathSum(x, y):
            if not inBounds(x,y):
                return float('inf')
            if (x, y) in dp:
                return dp[(x,y)]
            if x == len(matrix) - 1:
                return matrix[x][y]
            bottom = pathSum(x+1,y) 
            left = pathSum(x+1, y-1) 
            right = pathSum(x+1,y+1) 
            minimum = min([bottom, left, right])
            result = (matrix[x][y] + minimum)
            dp[(x,y)] = result
            return result
        
        minPathSum = float('inf')
        for i in range(len(matrix[0])):
            # print('i ',i)
            pathSumValue = pathSum(0, i)
            minPathSum = min(minPathSum, pathSumValue)
        return minPathSum
        
matrix = [[-19,57],[-40,-5]]
Solution().minFallingPathSum(matrix)
                     