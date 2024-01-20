from typing import List
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key= lambda x:x[0])
        intervals = sorted(intervals, key = lambda x:x[1], reverse=True)
        total_length = len(intervals)
        reduced_length = 0
        
        for i in range(total_length):
            j = i + 1
            while j < total_length and ((intervals[i][0] <= intervals[j][0]) and (intervals[j][1] <= intervals[i][1]) ):
                j += 1
                reduced_length += 1
            i = j
        return (total_length - reduced_length)   


Solution().removeCoveredIntervals(intervals = [[1,2],[1,4],[3,4]])
        