from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set(nums)
        sortedNums = sorted(nums)
        sortedNums.reverse()
        for i in sortedNums:
            if -i in numSet:
                return i

        return -1


s = Solution()
print(s.findMaxK(nums=[-1, 10, 6, 7, -7, 1]))
