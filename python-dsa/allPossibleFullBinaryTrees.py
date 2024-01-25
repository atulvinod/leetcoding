from typing import List, Optional

'''
https://leetcode.com/problems/all-possible-full-binary-trees/
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = dict()
        def createTrees(num):
            if num % 2 == 0:
                return []
            if num == 1:
                return [TreeNode(0)]

            if num == 3:
                return [TreeNode(0, TreeNode(0), TreeNode(0))]
            
            if num in memo:
                return memo[num]
            
            result = []
            
            for root in range(2, num):
                leftTree = createTrees(root-1)
                rightTree = createTrees(num - root)
                for x in leftTree:
                    for y in rightTree:
                        subTree = TreeNode(0, x, y)
                        result.append(subTree)
            memo[num] = result
            return result
        allTrees = createTrees(n)
        return allTrees  
    
result = Solution().allPossibleFBT(7)
print(result)
            
