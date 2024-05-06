from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        result = [-1] * len(intervals)
        sortedArr = sorted(intervals[:], key=lambda x: x[0])
        originalMap = dict()

        for index, [start, end] in enumerate(intervals):
            originalMap[(start, end)] = index

        def binarySearch(target):
            l, r = 0, len(intervals) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                (x, _) = sortedArr[mid]
                if x == target:
                    return mid
                elif target < x:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        for i in range(len(intervals)):
            (_, target) = intervals[i]
            if target <= sortedArr[len(intervals) - 1][0]:
                searchResult = binarySearch(target)
                (x, y) = sortedArr[searchResult]
                result[i] = originalMap[(x, y)]
        return result


s = Solution()
print(
    s.findRightInterval(
        intervals=[[1, 12], [2, 9], [3, 10], [13, 14], [15, 16], [16, 17]]
    )
)
