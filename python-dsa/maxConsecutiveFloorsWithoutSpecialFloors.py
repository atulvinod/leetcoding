from typing import List
'''
https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors
'''
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        prev = bottom
        maxv = 0
        for i in special:
            if prev == i:
                prev = i + 1
                continue
            interval = ((i-1)-prev)+1
            maxv = max(interval, maxv)
            prev = i + 1
        if prev < top:
            maxv = max(top - prev + 1, maxv)
        return maxv
        
Solution().maxConsecutive(6,8,[7,6,8])