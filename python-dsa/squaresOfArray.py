from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = list(map(lambda x:x*x, nums))
        squares.sort()
        return squares
    
print(
Solution().sortedSquares([-7,-3,2,3,11]))
        