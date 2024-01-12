from typing import List
import heapq
from collections import Counter

'''
https://leetcode.com/problems/reorganize-string/
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        '''
            Counter is a datastructure used to find the count of occurences of each value
        '''
        map = Counter(s)
        heap = [ [-cnt, val] for [val, cnt] in map.items()]
        '''
            heap uses the first value to compare in case of arrays
        '''
        
        heapq.heapify(heap)
        
        '''
            the approach that we use is to not use the last used character used to create the result array
        '''
        previous = None
        result = []
        while len(heap) != 0:
            [count, character] = heapq.heappop(heap)
            result.append(character)
            count += 1
            '''
                readd the previous character into the heap when we have used the other element
            '''
            if previous is not None:
                heapq.heappush(heap,previous)
                previous = None
                
            '''
                To become the previous, the count should not be zero
            '''
            if count != 0:
                previous = [count, character] 
            
        result = ''.join(result)
        return "" if len(result) != len(s) else result
        
print(Solution().reorganizeString("aaab"))