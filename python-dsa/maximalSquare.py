from typing import List

# at every point, we check if the current cell is 1, if it is then we can create at least a square of size 1, then we check the maximum square that we can create at right, down and diagonal. Then we take the minimum of those and add 1, as the current cell will  contribute one to the size 

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix) , len(matrix[0])
        cache = {}

        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            if (r, c) not in cache:
                
                down = helper(r+1, c)
                right = helper(r, c+1)
                diag = helper(r+1, c+1)

                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diag)

            return cache[(r, c)]
    
        helper(0,0)
        return max(cache.values())**2