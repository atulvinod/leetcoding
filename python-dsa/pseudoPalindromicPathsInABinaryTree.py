from typing import Optional
from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        result = 0 
        def solve(node, currentPath:dict):
            nonlocal result
            if node is None:
                return
            if node.left is None and node.right is None:
                if node.val in currentPath:
                    currentPath[node.val] += 1
                else:
                    currentPath[node.val] = 1
                oddValueCounts = 0
                for v in currentPath.values():
                    if v % 2 != 0:
                        oddValueCounts += 1
                if oddValueCounts <= 1:
                    result += 1
                currentPath[node.val] -= 1
                return 
            if node.val in currentPath:
                currentPath[node.val] += 1
            else:
                currentPath[node.val] = 1
            solve(node.left, currentPath)
            solve(node.right, currentPath)
            currentPath[node.val] -= 1

        solve(root, dict())
        return result
    
    
tree = TreeNode(2, TreeNode(3, TreeNode(3), TreeNode(1)),TreeNode(1, None, TreeNode(1)))
sol = Solution()
sol.pseudoPalindromicPaths(tree)