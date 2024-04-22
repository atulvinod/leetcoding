from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for index, element in enumerate(nums):
            map[element] = index
        for index, element in enumerate(nums):
            t = target - element
            if t in map and map[t] != index:
                return [index, map[t]]


s = Solution()
print(s.twoSum(nums=[2, 7, 11, 15], target=9))
