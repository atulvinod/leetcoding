from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        vectors = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def isOutOfBounds(row, col):
            return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    for [x, y] in vectors:
                        newRow, newCol = x + row, y + col
                        if isOutOfBounds(newRow, newCol) or grid[newRow][newCol] == 0:
                            perimeter = perimeter + 1
                            
        return perimeter


s = Solution()
print(s.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
