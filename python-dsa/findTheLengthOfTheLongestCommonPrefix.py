from typing import List

class Node:
    def __init__(self, character) -> None:
        self.neighbours = dict()
        self.character = character
        self.match = None

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        root = Node('')
        maxdepth = 0

        for x in arr1:
            current = root
            for c in str(x):
                if c not in current.neighbours:
                    current.neighbours[c] = Node(c)
                current = current.neighbours[c]

        for x in arr2:
            current = root
            for c in str(x):
                if c not in current.neighbours:
                    node = Node(c)
                    current.neighbours[c] = node 
                    node.match = False
                else:
                    if current.neighbours[c].match is None:
                        current.neighbours[c].match = True 
                current = current.neighbours[c]
        
        def traverse(rootNode: Node, depth: int):
            nonlocal maxdepth
            if rootNode.match:
                maxdepth = max(maxdepth, depth)
            
            for n in rootNode.neighbours.values():
                traverse(n, depth+1)

        for n in root.neighbours.values():
            traverse(n, 1)

        return maxdepth
    

Solution().longestCommonPrefix(arr1 = [1,10,100], arr2 = [1000])