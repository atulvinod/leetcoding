from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx, ans, l, r, n = max(nums), 0, 0, 0, len(nums)
        while r < n:
            k -= nums[r] == mx
            r += 1
            while k == 0:
                k += nums[l] == mx
                l += 1
            ans += l
        return ans


Solution().countSubarrays(nums=[1, 3, 2, 3, 3], k=2)
