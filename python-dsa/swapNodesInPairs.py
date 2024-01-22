'''
https://leetcode.com/problems/swap-nodes-in-pairs
'''
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        def swapper(prev, current):
            nonlocal new_head
            if current is None or current.next is None:
                return
            
            current_node = current
            next_node = current.next
            next_next_node = next_node.next if next_node is not None else None

            current_node.next = next_next_node
            
            if next_node is not None:
                next_node.next = current_node

            if prev is not None:
                prev.next = next_node
            if new_head is None:
                new_head = next_node
            
            swapper(current_node, next_next_node)

        
        swapper(None , head)
        return head if new_head is None else new_head
    

l_list = ListNode(1, ListNode(2, ListNode(3)))
Solution().swapPairs(l_list)
