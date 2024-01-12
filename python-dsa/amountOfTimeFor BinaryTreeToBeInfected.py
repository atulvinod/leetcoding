import queue
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    '''
        we convert the tree representation to a graph by traversing the tree and adding
        the edges to an adjacency list. after that we do a bfs search from the start point.
    '''
    def amountOfTime(self, root: Optional[TreeNode], start: TreeNode) -> int:
        adjMap = {}
        minutes = 0
        visited = {}
        visited[start] = True
        bfsQueue = queue.Queue()

        def traverse(node):
            if node is None:
                return
            
            if not node.val in adjMap:
                adjMap[node.val] = [] 

            if node.left is not None:
                adjMap[node.left.val] = []
                adjMap[node.val].append(node.left.val)
                adjMap[node.left.val].append(node.val)

            if node.right is not None:
                adjMap[node.right.val] = [] 
                adjMap[node.val].append(node.right.val)
                adjMap[node.right.val].append(node.val)

            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
        bfsQueue.put(start)

        while not bfsQueue.empty():
            length = bfsQueue.qsize()
            print(f"{list(bfsQueue.queue)} {minutes}")
            while length != 0:
                node = bfsQueue.get()
                visited[node] = True
                length -= 1
                neighbors = adjMap[node]
                for n in neighbors:
                    if n not in visited or not visited[n]:
                        bfsQueue.put(n) 
            minutes += 1

        return (minutes-1)

result = Solution().amountOfTime(TreeNode(1, TreeNode(5,None, TreeNode(4, TreeNode(9), TreeNode(2))), TreeNode(3, TreeNode(10),TreeNode(6))),3)