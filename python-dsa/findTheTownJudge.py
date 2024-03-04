from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adjMatrix = dict()
        for i in range(1, n+1):
            adjMatrix[i] = set()
        for [x, y] in trust:
            adjMatrix[x].add(y)

        zeroConnectionKeys = [key for key, value in adjMatrix.items() if len(value) == 0]
        for k in zeroConnectionKeys:
            connected = True
            for m, ne in adjMatrix.items():
                if m != k and k not in ne:
                    connected = False
            if connected:
                return k 
        
        return -1

Solution().findJudge(n = 3, trust = [[1,3],[2,3]])