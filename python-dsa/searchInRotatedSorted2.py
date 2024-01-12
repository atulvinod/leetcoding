from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0 , len(nums) - 1
        while (l <= r):
            mid = l + ( r - l) // 2
            if target == nums[mid]:
                return True
            '''
                when mid is greater than the left, then it implies that the left size of the array 
                is sorted, else the right side of the array is sorted and we check if the target lies 
                in that range,
                when left is equal to right, then we cannot decide which side to go , hence we increase the left
                and check again
            '''
            if nums[l] < nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] > nums[mid]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                l += 1
    
        return False
               