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


def printLinkedList(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next
