from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def solve(currentArr):
            if len(currentArr) == k:
                if sum(currentArr) == n:
                    result.append(currentArr[:])
                return
                
            if len(currentArr) > k:
                return
            
            prevNumber = 0 if len(currentArr) == 0 else currentArr[-1]
            
            for i in range(prevNumber+1, 10):
                currentArr.append(i)
                solve(currentArr)
                currentArr.pop() 
        solve([])
        return result

Solution().combinationSum3(3,9)