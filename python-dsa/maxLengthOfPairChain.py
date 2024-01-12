from typing import List

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs,key = lambda x: x[1])
        result = [1] * len(pairs)
        result[(len(pairs))-1] = 1
        for i in range(len(pairs)-1, -1, -1):
            for j in range(i, len(pairs)):
                if pairs[i][1] < pairs[j][0]:
                    # print(f"{i}, {j}")
                    result[i] = result[j] + 1
                    break
                
        return max(result)
        
# Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]])PR
print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))