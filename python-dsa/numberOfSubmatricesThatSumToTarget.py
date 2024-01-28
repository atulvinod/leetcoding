from typing import List
'''
#important
'''
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        columnWiseSumPrefix = [[0]*(cols+1) for _ in range((rows))]
        
        for row in range(0,rows):
            columnWiseSumPrefix[row][1] = matrix[row][0]
            for col in range(2, cols+1):
                columnWiseSumPrefix[row][col] = matrix[row][col-1] + columnWiseSumPrefix[row][col-1]

        subMatriceCount = 0
        for colStart in range(1, cols+1):
            for colEnd in range(colStart, cols+1):
                for rowStart in range(0, rows):
                    sum = 0
                    for rowEnd in range(rowStart, rows):
                        queryValue = columnWiseSumPrefix[rowEnd][colEnd] -  columnWiseSumPrefix[rowEnd][colStart-1]
                        sum += queryValue
                        if target == sum:
                            subMatriceCount += 1
                        
        
        return subMatriceCount
                                     
        
        
Solution().numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]]
, target = 0)