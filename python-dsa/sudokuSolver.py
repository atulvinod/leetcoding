from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        v = [2,5,8]
        
        box_ranges = [[x,y] for x in v for y in v]
        row = {n:set() for n in range(0, len(board))}
        col = {n: set() for n in range(0, len(board[0]))}
        box = {n : set() for n in range(9)}
        
        def getBox(x,y):
            for i in range(len(box_ranges)):
                [r_x, r_y] = box_ranges[i]
                if x <= r_x and y <= r_y:
                    return i
            return None
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != '.':
                    board[r][c] = (board[r][c])
                    row[r].add(board[r][c])
                    col[c].add(board[r][c])
                    box[getBox(r,c)].add(board[r][c])
                
        def solve(x, y):
            if x >= len(board):
                return True
            if y >= len(board[0]):
                return solve(x+1, 0)

            if board[x][y] != ".":
                return solve(x, y+1)
                            
            cur_box = getBox(x, y)
            for i in range(1, 10):
                value = str(i)
                if value not in row[x] and value not in col[y] and value not in box[cur_box]:
                    board[x][y] = value
                    row[x].add(value)
                    col[y].add(value)
                    box[cur_box].add(value)
                    result = solve(x, y+1)
                    if result:
                        return True
                    row[x].remove(value)
                    col[y].remove(value)
                    box[cur_box].remove(value)
                    board[x][y] = '.'
            return False
        solve(0,0)



board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
print(board)