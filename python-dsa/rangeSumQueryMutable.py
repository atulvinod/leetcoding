from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.bitTree = self.createTree(self.array)

    def createTree(self, array):
        bitTree = [0] * (len(array) + 1)

        def update(index, delta):
            while index < len(bitTree):
                bitTree[index] += delta
                index += index & -index

        for n in range(1, len(array) + 1):
            update(n, array[n - 1])
        return bitTree

    def update(self, index: int, val: int) -> None:
        delta = val - self.array[index]
        index = index + 1
        while index < len(self.bitTree):
            self.bitTree[index] += delta
            index += index & -index

    def sumRange(self, left: int, right: int) -> int:
        left = left
        right = right + 1

        def sum(index):
            ans = 0
            while index > 0:
                ans += self.bitTree[index]
                index -= index & -index
            return ans

        return sum(right) - sum(left)


# Your NumArray object will be instantiated and called as such:
numArray = NumArray([1, 3, 5])
print(numArray.sumRange(0, 2))
numArray.update(1, 2)
print(numArray.sumRange(0, 2))
