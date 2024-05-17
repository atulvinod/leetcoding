class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def linkedListBuilder(array):
    head = None
    current = None
    for i in array:
        if head is None:
            head = ListNode(i)
            current = head
        else:
            current.next = ListNode(i)
            current = current.next
    return head


def treeBuilder(array):
    map = dict()
    for i in range(len(array)):
        if array[i] is None:
            continue

        left = 2 * i + 1
        right = 2 * i + 2
        root = None

        if i not in map or map[i] is None:
            map[i] = TreeNode(array[i])

        root = map[i]
        if left <= len(array) - 1 and array[left] is not None:
            left_node = None
            if left not in map or map[left] is None:
                map[left] = TreeNode(array[left])
            left_node = map[left]
            root.left = left_node

        if right <= len(array) - 1 and array[right] is not None:
            right_node = None
            if right not in map or map[right] is None:
                map[right] = TreeNode(array[right])
            right_node = map[right]
            root.right = right_node
    return map[0]


def printLinkedList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next
