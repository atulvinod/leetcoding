
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # to handle no root case
        if root is None:
            return 0

        # to handle the leaf
        if root.left is None and root.right is None:
            return 1
        
        # to conditionaly traverse the nodes, if there is no left or right nodes, then we dont traverse the node 
        left, right = float('inf'), float('inf')
        if root.left is not None:
            left = self.minDepth(root.left)

        if root.right is not None:
            right = self.minDepth(root.right)

        return 1 + min(left, right)