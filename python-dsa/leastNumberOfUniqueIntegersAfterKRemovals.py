from typing import List
from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        heap = [(freq, val) for [val, freq] in Counter(arr).items()]
        heapq.heapify(heap)

        while (k > 0):
            (freq, val) = heapq.heappop(heap)
            if k >= freq:
                k -= freq
            else:
                new_k = k - freq
                new_freq = freq - k
                k = new_k
                heapq.heappush(heap, (new_freq, val))
        
        return len(heap)
    

Solution().findLeastNumOfUniqueInts(arr =[1,2,2,2,2],k =
4)