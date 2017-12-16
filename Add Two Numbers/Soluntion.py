# coding: utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        _t = head
        while l1 != None or l2 != None or _t.val > 0:
            f = (lambda x: x.val if not x is None and not x.val is None else 0)
            _v = f(l1) + f(l2) + f(_t)
            _t.val = _v % 10
            _p = _v // 10
            if _p > 0:
                _n = ListNode(_p)
            else:
                if (l1 != None and l1.next !=None) or (l2 != None and l2.next !=None):
                    _n = ListNode(None)
                else:
                    return head
            _t.next = _n
            _t = _t.next
            l1 = l1.next if not l1 is  None else None
            l2 = l2.next if not l2 is  None else None