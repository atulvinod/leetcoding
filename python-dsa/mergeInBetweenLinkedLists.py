from typing import List
from utils import linkedListBuilder, ListNode, printLinkedList


class Solution:
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:

        list2Head = list2
        list2Tail = list2

        while list2Tail.next is not None:
            list2Tail = list2Tail.next

        index = 1
        list1InsertHead = list1

        while index != a:
            list1InsertHead = list1InsertHead.next
            index = index + 1

        list2InsertTail = list1InsertHead.next

        while index != b:
            list2InsertTail = list2InsertTail.next
            index = index + 1

        list2InsertTail = list2InsertTail.next
        list1InsertHead.next = list2Head
        list2Tail.next = list2InsertTail

        return list1


list1 = linkedListBuilder([10, 1, 13, 6, 9, 5])
list2 = linkedListBuilder([1000000, 1000001, 1000002])

result = Solution().mergeInBetween(list1=list1, a=3, b=4, list2=list2)
printLinkedList(result)
