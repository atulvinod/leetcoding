from typing import List
import heapq
from collections import Counter

class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        joinedWord = ''.join(words)
        pairHeap = [-(freq // 2) for freq in Counter(joinedWord).values()]
        characterHeap = [ -(freq % 2) for freq in Counter(joinedWord).values()]
        wordLengthHeap = [len(i) for i in words]
        heapq.heapify(pairHeap)
        heapq.heapify(wordLengthHeap)
        heapq.heapify(characterHeap)

        result = 0
        while len(wordLengthHeap) > 0:
            lenValue = heapq.heappop(wordLengthHeap)
            reqPairs = lenValue // 2
            reqCharacters = lenValue % 2
            if reqPairs != 0:
                pairHeapValue = -heapq.heappop(pairHeap)
                if pairHeapValue >= reqPairs:
                    heapq.heappush(pairHeap ,-(pairHeapValue-reqPairs))
                    reqPairs = 0
            if reqCharacters != 0:
                characterHeapValue = -heapq.heappop(characterHeap)
                if characterHeapValue >= reqCharacters:
                    heapq.heappush(characterHeap, -(characterHeapValue-reqCharacters))
                    reqCharacters = 0

            if reqCharacters == 0 and reqPairs == 0:
                result +=1

        return result
    

Solution().maxPalindromesAfterOperations(words = ["aa","bc"])