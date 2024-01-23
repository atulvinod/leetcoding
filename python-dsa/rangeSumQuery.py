from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.range = [0]*len(nums)
        self.range[0] = nums[0]
        for i in range(1, len(nums)):
            self.range[i] = nums[i] + self.range[i-1]
                

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.range[right]
        return self.range[right] - self.range[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

q = NumArray([-2, 0, 3, -5, 2, -1])
print(q.sumRange(0,2))
print(q.sumRange(2,5))
print(q.sumRange(0,5))