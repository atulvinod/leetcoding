from utils import ListNode, printLinkedList, linkedListBuilder
from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def rev(node: ListNode):
            if node.next is None:
                return (node, node)

            (new_head, next_node) = rev(node.next)
            next_node.next = node
            return (new_head, node)

        (new_head, _) = rev(head)
        head.next = None
        return new_head


node = linkedListBuilder([1, 2, 3, 4, 5])
printLinkedList(Solution().reverseList(node))
