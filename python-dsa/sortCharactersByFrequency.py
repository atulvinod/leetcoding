from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        char_count = Counter(s)
        heap = [(-v, c) for c,v in char_count.items()]
        heapq.heapify(heap)
        result = ""
        while len(heap) > 0:
            (v, c) = heapq.heappop(heap)
            result += c*(-v) 
            
        return result
    
    
Solution().frequencySort("tree")