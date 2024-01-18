from typing import List
from collections import Counter

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(len(garbage)):
            garbage[i] = Counter(garbage[i])

        total_cost = 0
        for g in ['M','P','G']:
            last_loc = 0
            current_cost = 0
            for i in range(len(garbage)):
                if g in garbage[i]:
                    current_cost += garbage[i][g]
                    garbage[i][g] = 0
                    while last_loc != i:
                        current_cost += travel[last_loc]
                        last_loc += 1
            total_cost += current_cost
        return total_cost


Solution().garbageCollection(garbage = ["MMM","PGM","GP"], travel = [3,10])