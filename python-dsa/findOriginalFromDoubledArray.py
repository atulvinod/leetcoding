from typing import List
from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        length = len(changed)
        if length % 2 != 0:
            return []
        required = length // 2
        value_counts = Counter(changed)
        sorted_values = sorted(value_counts.keys())
        result = []
        for v in sorted_values:
            if (value_counts[v]) <= 0:
                continue
            if v == 0:
                if value_counts[v] % 2 == 0:
                    result.extend([0]*(value_counts[v] // 2))      
            elif v * 2 in value_counts and value_counts[v*2] > 0:
                reduce_by = min(value_counts[v], value_counts[v*2])
                value_counts[v] -= reduce_by
                value_counts[v*2] -= reduce_by
                result.extend([v]*reduce_by)
        return result if len(result) == required else []
    
Solution().findOriginalArray(changed = [0,0,0,0]
)