from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)
        
        for startIndex in range(len(nums1)):
            i = startIndex
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    result = set()
                    while j < len(nums2) and i < len(nums1) and nums2[j] == nums1[i]:
                        result.add(nums1[i])
                        i += 1
                        j += 1
                    return list(result)
        return []

Solution().intersection(nums1 = [1,2,2,1], nums2 = [2,2])
                        