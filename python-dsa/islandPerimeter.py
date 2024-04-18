from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = dict()

        perimeter = 0
        vectors = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        def isOutOfBounds(row, col):
            return row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0])

        def dfs(row, col):
            nonlocal visited
            nonlocal vectors
            nonlocal perimeter
            if isOutOfBounds(row, col) or grid[row][col] == 0 or (row, col) in visited:
                return

            visited[(row, col)] = True

            for [x, y] in vectors:
                newRow, newCol = x + row, y + col
                if isOutOfBounds(newRow, newCol) or grid[newRow][newCol] == 0:
                    perimeter = perimeter + 1
                else:
                    dfs(newRow, newCol)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    break

        return perimeter


s = Solution()
print(s.islandPerimeter(grid=[[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]))
