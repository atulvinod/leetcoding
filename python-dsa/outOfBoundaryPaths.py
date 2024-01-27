modulo = 10**9+7

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # matrix = [ [0]*n for _ in range(m)]
        
        vectors = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]
        
        memo = dict()
        
        def isInBounds(x,y):
            return x >= 0 and x < m and y >= 0 and y < n 
        
        def solve(x, y, currentMoves):
            if not isInBounds(x,y):
                return 1
            if currentMoves == 0:
                return 0
            if (x,y,currentMoves) in memo:
                return memo[(x,y,currentMoves)]
            
            totalPaths = 0
            for _x, _y in vectors:
                result = solve(x+_x, y+_y, currentMoves-1)
                totalPaths = (totalPaths+ result)%modulo
            memo[(x,y,currentMoves)] = totalPaths
            return totalPaths
        
        result = solve(startRow, startColumn, maxMove)
        return result
    

obj = Solution()
print(obj.findPaths(m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1))
            
         