# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        first = head.next
        if first is None:
            return False
        second = head.next.next

        while not second is None:
            if first.val == second.val:
                return True

            first = first.next
            if first is None:
                return False

            if second.next is None:
                return False
            second = second.next.next

        return False