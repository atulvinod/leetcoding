from typing import List
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0]*n
        matrix = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]        
        for i in range(1, n):
            matrix[i][i+1] = 1
            matrix[i+1][i] = 1
            print(matrix)
        
        for i in range(1, n+1):
            matrix[i][i] = 0
        
        if x != y:
            matrix[x][y] = 1
            matrix[y][x] = 1
        
        for current in range(1, n+1):
            for i in range(1,n+1):
                for j in range(1, n+1):
                    matrix[i][j] = min(matrix[i][j], matrix[i][current]+matrix[current][j])

        for i in range(1, n+1):
            for j in range(1, n+1):
                if i  == j:
                    continue
                result[matrix[i][j]-1] += 1
        return result



Solution().countOfPairs(3,1,3)