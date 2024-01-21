'''
https://leetcode.com/problems/pascals-triangle-ii
'''
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex+1):
            temp = [1]*(i+1)
            for j in range(1, len(triangle)):
                temp[j] = triangle[j] + triangle[j-1]
            triangle = temp
        
        return triangle
    
    
Solution().getRow(3)