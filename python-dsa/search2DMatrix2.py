from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(array: List[int]):
            l, r = 0, len(array) - 1
            while l <= r:

                mid = l + ((r - l) // 2)
                if array[mid] == target:
                    return True
                elif array[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1

            return False

        for row in range(len(matrix)):
            if matrix[row][0] <= target <= matrix[row][len(matrix[row]) - 1]:
                search = binarySearch(matrix[row])
                if search:
                    return True

        return False


s = Solution()
print(
    s.searchMatrix(
        matrix=[[5], [6]],
        target=6,
    )
)
