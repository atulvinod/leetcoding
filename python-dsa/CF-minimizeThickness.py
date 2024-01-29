from typing import List

def findMinThickness(nums: List[int]):
    prefixSum = [0]*(len(nums)+1)
    prefixSum[1] = nums[0]
    for i in range(1, len(prefixSum)):
        prefixSum[i] = prefixSum[i-1] + nums[i-1]
    
    minThickNess = float('inf')
    def solve(l, r, prevSum = None):
        nonlocal minThickNess
        if l >= len(prefixSum):
            return -float('inf')
        for i in range(l,r):
            sum = prefixSum[i] - prefixSum[l-1]
            if prevSum is None:
                result = solve(i+1, r, sum)
                if result is not None:
                    minThickNess = min(max(i-l+1, result), minThickNess)
            else:
                if sum == prevSum:
                    result = solve(i+1, r, sum)
                    if result is not None:
                        maxThickNess = max(i-l+1, result)
                        return maxThickNess
                if sum > prevSum:
                    return None
        return None
    
    solve(1, len(prefixSum))
    return minThickNess


findMinThickness([1 for _ in range(2000)])
# cases = int(input())
# while cases > 0:
#     n = int(input())
#     num_input = input().split(' ')
#     numbers = [ int(i) for i in num_input]
#     result = findMinThickness(numbers)
#     print(result)
#     cases -= 1