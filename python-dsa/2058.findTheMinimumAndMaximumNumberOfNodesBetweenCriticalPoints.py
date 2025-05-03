from typing import Optional, List
from utils import linkedListBuilder, ListNode


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1, -1]
        lowestCrit = None
        highestCrit = None
        prevCrit = None
        ptr = head
        prev: Optional[ListNode] = None
        index = 0
        minCritDistance = float("inf")
        critPointCount = 0
        while ptr != None:
            if prev != None and ptr.next != None:
                prevVal = prev.val
                nextVal = ptr.next.val
                current = ptr.val
                if (prevVal > current < nextVal) or (prevVal < current > nextVal):
                    critPointCount = critPointCount + 1
                    if lowestCrit == None:
                        lowestCrit = index
                    highestCrit = index
                    if prevCrit != None:
                        minCritDistance = min(abs(index - prevCrit), minCritDistance)
                    prevCrit = index
            prev = ptr
            ptr = ptr.next
            index = index + 1
        if critPointCount > 1:
            if lowestCrit != None and highestCrit != None:
                result[1] = abs(lowestCrit - highestCrit)
            if prevCrit != None:
                result[0] = minCritDistance

        return result


list = linkedListBuilder([2, 2, 1, 3])
print(Solution().nodesBetweenCriticalPoints(list))
