'''
https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i
'''
from typing import List

class Solution:
    def minimumPushes(self, word: str) -> int:
        keypad = [0]*8
        current_index = 0
        mapped_keys = dict()
        cost = 0
        for c in word:
            if c in mapped_keys:
                cost += mapped_keys[c]
            else:
                keypad[current_index] += 1
                cost += keypad[current_index]
                mapped_keys[c] = keypad[current_index]
                current_index = (current_index +1)%8
        return cost

Solution().minimumPushes("xycdefghij")