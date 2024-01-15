from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loserMapCount = dict()
        winnerSet = set()
        loserSet = set()
        for [winner, loser] in matches:
            winnerSet.add(winner)
            loserSet.add(loser)
            loserMapCount[loser] = 1 if loser not in loserMapCount else loserMapCount[loser] + 1
        onlyWinners = list(winnerSet.difference(loserSet))
        oneMatchLosers = [ key for [key, value] in loserMapCount.items() if value == 1 ]
        oneMatchLosers.sort()
        onlyWinners.sort()
        return [onlyWinners, oneMatchLosers]
        
Solution().findWinners([[2,3],[1,3],[5,4],[6,4]])
                        