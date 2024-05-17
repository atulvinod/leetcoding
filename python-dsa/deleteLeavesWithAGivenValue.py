from typing import Optional
from utils import TreeNode, treeBuilder


class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def processTree(node: TreeNode):
            if node is None:
                return True
            if node.left is None and node.right is None:
                return target == node.val

            doDeleteLeft = processTree(node.left)
            doDeleteRight = processTree(node.right)

            if doDeleteLeft:
                node.left = None

            if doDeleteRight:
                node.right = None

            return doDeleteLeft and doDeleteRight and node.val == target

        doDeleteRoot = processTree(root)
        if doDeleteRoot:
            return None
        return root


root = treeBuilder([1, 2, 3, 2, None, 2, 4])
target = 2
result = Solution().removeLeafNodes(root, target)
