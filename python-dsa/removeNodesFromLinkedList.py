from utils import ListNode, linkedListBuilder
from typing import Optional


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newNodes = []

        def traverse(node: ListNode):
            nonlocal newNodes
            if node.next is None:
                newNodes.append(node)
                return node.val
            maxNode = traverse(node.next)
            if node.val >= maxNode:
                newNodes.append(node)
            return max(node.val, maxNode)

        traverse(head)
        for n in range(len(newNodes) - 1, 0, -1):
            node = newNodes[n]
            nextNode = newNodes[n - 1]
            node.next = nextNode

        return newNodes[len(newNodes) - 1]


head = [5, 2, 13, 3, 8]
linkedList = linkedListBuilder(head)
s = Solution()
s.removeNodes(linkedList)
