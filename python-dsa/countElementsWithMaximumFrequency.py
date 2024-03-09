from collections import Counter
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        maxFreq = -1
        maxFreqNums = []

        for k, v in freq.items():
            if v > maxFreq:
                maxFreq = v
                maxFreqNums = []
                maxFreqNums.append(v)
            elif v == maxFreq:
                maxFreqNums.append(v)

        return sum(maxFreqNums)


Solution().maxFrequencyElements([1, 2, 3, 4, 5])
