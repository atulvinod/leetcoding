from typing import List
class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        result = [0]*n
        matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]        
        for i in range(1, n):
            matrix[i][i+1] = 1
            matrix[i+1][i] = 1
            print(matrix)
        
        for current in range(1, n+1):
            for i in range(1,n+1):
                for j in range(1, n+1):
                    matrix[i][j] = min(matrix[i][j], matrix[i][current]+matrix[current][j])

        print(matrix)



Solution().countOfPairs(3,1,3)