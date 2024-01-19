from collections import Counter
from typing import List
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        task_count = Counter(tasks)
        rounds = 0
        for value in task_count.values():
            if (value % 3) % 2 == 0:
                rounds += value // 3
                rounds += (value % 3) // 2
            elif value % 3 == 0:
                rounds += value // 3
            elif value % 2 == 0:
                rounds += value // 2
            else:
                return -1
            
        return rounds

Solution().minimumRounds([66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61])