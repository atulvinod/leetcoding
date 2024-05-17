from typing import Optional
from utils import TreeNode, treeBuilder


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def solve(node: TreeNode):
            if node is None:
                return True
            if node.left is None and node.right is None:
                return target == node.val

            leftResult = solve(node.left)
            rightResult = solve(node.right)

            if leftResult:
                node.left = None

            if rightResult:
                node.right = None

            return leftResult and rightResult and node.val == target

        result = solve(root)
        if result:
            return None
        return root


root = treeBuilder([1, 2, 3, 2, None, 2, 4])
target = 2
result = Solution().removeLeafNodes(root, target)
