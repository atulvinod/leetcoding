from typing import Optional
from utils import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        result = None

        def dfs(node: TreeNode, current: str):
            if node is None:
                return

            if node.left is None and node.right is None:
                current = chr(ord("a") + node.val) + current
                if result is None:
                    result = current
                else:
                    result = min(result, current)
                return

            dfs(node.left, chr(ord("a") + node.val) + current)
            dfs(node.right, chr(ord("a") + node.val) + current)

        dfs(root, "")
        return result
