
from typing import List


class Solution:
    def minimizeArrayScore(self, n : int, arr : List[int]) -> int:
        # code here
        sorted_arr_min = sorted(arr)
        sorted_arr_max = sorted(arr, reverse=True)
        op_count = n // 2
        max_v = -float('inf')
        i = 0
        while i < op_count:
            x = sorted_arr_min[i]
            y = sorted_arr_max[i]
            max_v = max(x+y, max_v)
            i += 1
            
        return max_v
    
    

Solution().minimizeArrayScore(4,[6,4,3,4])
                    
