from utils import ListNode, linkedListBuilder, printLinkedList


class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        numsSet = set(nums)
        prev: ListNode = None
        current: ListNode = head
        nonRemovedHead = None

        while current:
            if current.val in numsSet:
                # removing head
                if prev is None:
                    current = current.next
                    continue
                prev.next = current.next
                current = current.next
            else:
                if prev is None:
                    if nonRemovedHead is None:
                        nonRemovedHead = current
                prev = current
                current = current.next

        return nonRemovedHead


nums = [1]
head = [1, 2, 1, 2, 1, 2]
updatedHead = Solution().modifiedList(nums, linkedListBuilder(head))
printLinkedList(updatedHead)
