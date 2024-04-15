from typing import List

numbers = [0] * 101
for i in range(2, 101):
    if numbers[i] == 0:
        k = 2
        n = i * k
        while n < 101:
            numbers[n] = 1
            k = k + 1
            n = i * k


class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < len(nums):
            if nums[l] != 1 and numbers[nums[l]] == 0:
                break
            l = l + 1
        while r >= 0:
            if nums[r] != 1 and numbers[nums[r]] == 0:
                break
            r = r - 1

        return abs(l - r)


s = Solution()
print(s.maximumPrimeDifference(nums=[4, 2, 9, 5, 3]))
