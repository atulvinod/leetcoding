from typing import List
from collections import Counter
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # to maintain the current set of characters
        currentCharSet = set()
        
        # to check if the new string overlaps with the character set
        def overlap(charset, s):
            c = Counter(charset) + Counter(s)
            return max(c.values()) > 1
        
        def backtrack(i):
            if i == len(arr):
                return len(currentCharSet)
            
            currentResult = 0
            # if the new string does not overlap with the currently selected characters
            # we include the string in our resultset
            if not overlap(currentCharSet, arr[i]):
                for c in arr[i]:
                    currentCharSet.add(c)
                # execute the backtrack selecting the current string
                currentResult = backtrack(i+1)
                
                # remove the selected string's characters
                for c in arr[i]:
                    currentCharSet.remove(i)
            # return the max result from the selcted and non selected function results
            return max(currentResult, backtrack(i+1))

        return backtrack(0)
    
Solution().maxLength( arr =["cha","r","act","ers"])