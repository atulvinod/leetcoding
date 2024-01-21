class Treenode:
    def __init__(self, start, end, value = -float('inf')) -> None:
        self.start = start
        self.end = end
        self.value = value
        self.left = None
        self.right = None
    def __str__(self) -> str:
        return (f"start:{self.start} end:{self.end}, value:{self.value}")



class SegmentTree:
    def __init__(self, array) -> None:
        self.array = array
        self.root = self.__createTree(array)

    def __createTree(self, array):
        def generate(start, end):
            if start == end:
                node = Treenode(start, end, array[start])
                return (node, array[start])
            
            node = Treenode(start, end)
            mid = (start + end) // 2
            (left_node, left_node_value) = generate(start, mid, )
            (right_node, right_node_value) = generate(mid+1, end)
            node.left = left_node
            node.right = right_node
            max_value =  max(left_node_value, right_node_value)
            node.value = max_value
            return (node, max_value)
        
        (root, _) = generate(0, len(array)-1,1)
        return root
    
    def query(self, start, end):
        def _query(node):
            # for case where query is out of node range
            if start > node.end or end < node.start:
                return -float('inf')
             
            # for leaf case
            if node.start == node.end:
                return node.value
      
            # if node range is exactly in query range
            if  start <= node.start and node.end <= end:
                return node.value 
           
            #query lies partially in node range
            left_max = _query(node.left)
            right_max = _query(node.right)
            return max(left_max, right_max)

        result = _query(self.root)
        return result

    
array = [1,2,3,4,5,6,7]
max_segment_tree = SegmentTree(array)
# print(max_segment_tree.query(0, len(array)-1))
print(max_segment_tree.query(0,2))