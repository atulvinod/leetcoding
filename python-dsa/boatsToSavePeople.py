from typing import List
import heapq


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        heap = people[:]
        boatCount = 1
        currentBoat = 0
        heapq.heapify(heap)

        while len(heap) > 0:
            value = heapq.heappop(heap)
            if value + currentBoat > limit:
                boatCount += 1
                currentBoat = value
            else:
                currentBoat += value

        return boatCount


s = Solution()
print(s.numRescueBoats(people=[5, 1, 2, 4], limit=6))
