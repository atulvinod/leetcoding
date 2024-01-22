'''
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i
solution for 2nd part of this question as well, where repeating characters are used
'''
from typing import List
from collections import Counter
import heapq
class Solution:
    def minimumPushes(self, word: str) -> int:
        char_freq = Counter(word)
        heap = [(-v, k) for [k,v] in char_freq.items()]
        heapq.heapify(heap)
        keypad = [0]*8
        current_index = 0
        mapped_keys = dict()
        cost = 0
        
        while len(heap) != 0:
            (_, k) = heapq.heappop(heap)
            keypad[current_index] += 1
            mapped_keys[k] = keypad[current_index]
            current_index = (current_index + 1 )%8
        
        for c in word:
            cost += mapped_keys[c]


        return cost

Solution().minimumPushes("aabbccddeeffgghhiiiiii"
)