import math
'''
very typical question, using bucket sort and pigeonhole principle
https://leetcode.com/problems/maximum-gap/solutions/
https://www.youtube.com/watch?v=VT-6zwGKYwA&ab_channel=PrakashShukla
'''
class Solution:
    def maximumGap(self, num):
        if num is None or len(num) < 2:
            return 0

        # Get the max and min value of the array
        _min = min(num)
        _max = max(num)

        # The minimum possible gap, ceiling of the integer division
        gap = math.ceil((_max - _min) / (len(num) - 1))

        bucketsMIN = [float('inf')] * (len(num) - 1)  # store the min value in that bucket
        bucketsMAX = [float('-inf')] * (len(num) - 1)  # store the max value in that bucket

        # Put numbers into buckets
        for i in num:
            if i == _min or i == _max:
                continue
            idx = (i - _min) // gap  # index of the right position in the buckets
            bucketsMIN[idx] = min(i, bucketsMIN[idx])
            bucketsMAX[idx] = max(i, bucketsMAX[idx])

        # Scan the buckets for the max gap
        maxGap = float('-inf')
        previous = _min
        for i in range(len(num) - 1):
            if bucketsMIN[i] == float('inf') and bucketsMAX[i] == float('-inf'):
                # empty bucket
                continue
            # min value minus the previous value is the current gap
            maxGap = max(maxGap, bucketsMIN[i] - previous)
            # update previous bucket value
            previous = bucketsMAX[i]

        maxGap = max(maxGap, _max - previous)  # update the final max value gap
        return maxGap

