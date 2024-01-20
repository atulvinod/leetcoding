from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        value_counts = Counter(arr)
        value_sequence = sorted(value_counts.keys())
        result_count = 0
        for v in value_sequence:
            if v == 0 :
                if v % 2 != 0:
                    return False
                else:
                    result_count += value_counts[v]
                    continue
            if v*2 in value_counts and value_counts[v*2] > 0:
                reduce_by = min(value_counts[v], value_counts[v*2])
                value_counts[v] -= reduce_by
                value_counts[v*2] -= reduce_by
                result_count += reduce_by*2
        return result_count == len(arr)
            
Solution().canReorderDoubled([4,-2,2,-4])