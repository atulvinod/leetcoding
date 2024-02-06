from typing import List
from collections import Counter

import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        min_bound = len(nums) // 3
        heap = [(v,k) for [k,v] in Counter(nums).items()]
        
        result = []
        while len(heap) > 0:
            (v, k ) = heapq.heappop(heap)
            if v <= min_bound:
                continue
            result.append(k)
            
        return result
    
Solution().majorityElement([6,5,5])