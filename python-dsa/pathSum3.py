from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        def dfs(root, targetSum, path):
            if root == None: return None
            targetSum -= root.val
            path.append(root.val)
            if root.left == None and root.right == None:  # Is leaf node
                if targetSum == 0:  # Found a valid path
                    ans.append(path.copy())
            else:
                dfs(root.left, targetSum, path)
                dfs(root.right, targetSum, path)
            path.pop()  # backtrack

        ans = []
        dfs(root, targetSum, [])
        return ans
    
tree = TreeNode(5,TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(12), TreeNode(4, TreeNode(5),TreeNode(1))))
Solution().pathSum(tree, 22)