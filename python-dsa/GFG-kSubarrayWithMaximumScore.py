class Solution:
    def kMaxSubarray(self, n, k, arr):
        # Code Here.
        r = float('-inf')
        for i in range(len(n)):
            _sum = 0
            for j in range(i, n):
                if j - i < k:
                    _sum += arr[j]
                    r = max(r, _sum)
        return r