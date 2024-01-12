from typing import List, Dict

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        
        def permute(temp: List[int] ,visited: Dict , nums: List[int]):
            if(len(temp) == len(nums)):
                result.add(tuple(temp))
                return
            for i in range(len(nums)):
                if(i not in visited or not visited[i]):
                    temp.append(nums[i])
                    visited[i] = True
                    permute(temp, visited, nums)
                    visited[i] = False
                    temp.pop()
                    
        permute([],dict(), nums)
        result_arr = [list(n) for n in result]
        return result_arr        

Solution().permuteUnique([1,1,2])