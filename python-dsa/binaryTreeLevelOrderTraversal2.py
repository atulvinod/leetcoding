'''
#IMPORTANT
for binary level order traversal
'''
# Definition for a binary tree node.
import queue
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        result = []

        while not q.empty():
            length = q.qsize()
            result.append([ n.val for n in list(q.queue)])
            while length != 0:
                node = q.get()
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
                length -= 1
        return result[::-1]