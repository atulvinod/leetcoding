from typing import Optional
from utils import linkedListBuilder, ListNode


class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def sum(node: ListNode):
            if node is None:
                return 0
            extra = sum(node.next)
            sumv = node.val * 2 + extra
            node.val = sumv % 10
            carry = int(sumv / 10)
            return carry

        carry = sum(head)
        if carry != 0:
            newHead = ListNode(carry)
            newHead.next = head
            return newHead
        return head


head = [0]
node = linkedListBuilder(head)
s = Solution()
s.doubleIt(node)
