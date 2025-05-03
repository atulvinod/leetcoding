from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        uniqueTop = set(tops)
        uniqueBottom = set(bottoms)
        uniqueElements = list(uniqueTop.union(uniqueBottom))
        cost = float("inf")
        topCost = float('inf')
        bottomCost = float('inf');

        for index in range(len(uniqueElements) + 1):
      
            if (
                index == len(uniqueElements)
                and topCost is not None
                and bottomCost is not None
            ):
                cost = min(cost, min(topCost, bottomCost))
                break
            
            element = uniqueElements[index]
            skipMain = False
            tempTopCost = 0;
            tempBottomCost = 0;

            for index2 in range(0, len(tops)):
                if tops[index2] != element and bottoms[index2] != element:
                    skipMain = True
                    break
                if( tops[index2] != element):
                    tempTopCost = (tempTopCost + 1)
                if( bottoms[index2] != element):
                    tempBottomCost = (tempBottomCost + 1)
            if skipMain:
                continue
            
            topCost = min(topCost, tempTopCost)
            bottomCost = min(bottomCost, tempBottomCost)
            
        return -1 if cost == float('inf') else cost

tops = [1,1,1,1,1,1,1,1]
bottoms = [1,1,1,1,1,1,1,1]

print(Solution().minDominoRotations(tops, bottoms))