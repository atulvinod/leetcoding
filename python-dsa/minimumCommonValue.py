from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) > len(nums2):
            return self.getCommon(nums2, nums1)

        nums2set = set(nums2)
        for i in nums1:
            if i in nums2set:
                return i

        return -1


print(
    Solution().getCommon(
        [
            12,
            16,
            24,
            24,
            25,
            27,
            31,
            37,
            38,
            41,
            43,
            50,
            57,
            70,
            71,
            71,
            74,
            76,
            77,
            78,
        ],
        [5, 5, 9, 11, 12, 17, 20, 34, 36, 51, 61, 68, 70, 79, 85, 87, 88, 90, 91, 97],
    )
)
