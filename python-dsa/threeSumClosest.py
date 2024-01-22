'''
#IMPORTANT
https://leetcode.com/problems/3sum-closest/

we sort the array and take three pointers, "a" "b" and "c"
where "c" is the pointer at the end and "a" is at the start 
'''
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for first in range(len(nums)-2):
            a = nums[first]
            second = first+1
            end = len(nums) - 1
            while second < end:
                b = nums[second]
                c = nums[end]
                current_sum = a + b + c
                if current_sum == target:
                    return current_sum
                if abs(current_sum - target) < abs(target - closest):
                    closest = a + b + c
                if current_sum > target:
                    end-=1
                else:
                    second += 1

        return closest