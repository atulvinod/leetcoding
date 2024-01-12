from typing import Optional
'''
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def solve(root):
            if root is None:
                return None
            left = solve(root.left)
            right = solve(root.right)
            maxValue = -float('inf')
            minValue = float('inf')
            v = -float('inf')
            # print(f"root {root.val}, left: ${left} , right ${right}")
            if left is None and right is None:
                maxValue = root.val
                minValue = root.val
            if left is not None:
                maxValue = max(left['max'], maxValue)
                minValue = min(left['min'], minValue)
                v = max(abs(root.val - maxValue), abs(root.val-minValue), v, left['v'])
            if right is not None:
                maxValue = max(right['max'], maxValue)
                minValue = min(right['min'], minValue)
                v = max(abs(root.val - maxValue), abs(root.val-minValue), v, right['v'])
            # print(f"v {v} finalMax {max(maxValue, root.val)} finalMin {min(minValue, root.val)} \n")
            return {
                'max': max(maxValue, root.val),
                'min': min(minValue, root.val),
                'v': v
            }
        result = solve(root)
        return result['v']
    
# tree = TreeNode(8, TreeNode(3, TreeNode(1), TreeNode(6, TreeNode(4), TreeNode(7))), TreeNode(10, None, TreeNode(14, TreeNode(13))))

tree = TreeNode(1, None, TreeNode(2, None, TreeNode(0, TreeNode(3, None))))
Solution().maxAncestorDiff(tree)