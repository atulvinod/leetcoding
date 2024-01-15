'''
https://leetcode.com/problems/count-the-hidden-sequences/solutions/1711078/c-o-n-easy-solution-just-use-simple-math/
#important
'''
class Solution:
    def numberOfArrays(self, differences, lower, upper):
        max_diff = 0
        min_diff = 0
        num = 0

        for diff in differences:
            num += diff
            max_diff = max(max_diff, num)
            min_diff = min(min_diff, num)

        count = (upper - max_diff) - (lower - min_diff) + 1
        return max(0, count)
