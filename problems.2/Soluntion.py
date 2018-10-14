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

# --------------------------------------------------------------------------------#
# 犯了三个错误：
# 1. 直观的从头开始计算，结果导致为了维护尾，写了大量的判断代码，这里显然用一个空头开始，尾就非常好计算了
# 2. 进一位的值，我直接存到下一个节点里面去了，导致了要新增节点，又增加判断空节点的算法。其实用一个外部变量存是最好的
# 3. 取摸和取整，Python有一个divmod方法一次性做两个的
# --------------------------------------------------------------------------------#
# 下面是最佳实现：
# class Solution(object):
    # def addTwoNumbers(self, l1, l2):
    #     """
    #     :type l1: ListNode
    #     :type l2: ListNode
    #     :rtype: ListNode
    #     """
        
    #     dummy = ListNode(-1)
    #     tail = dummy
        
    #     carry = 0
    #     while l1 or l2 or carry:
    #         v1 = l1.val if l1 else 0
    #         v2 = l2.val if l2 else 0    
    #         carry, val = divmod(v1 + v2 + carry, 10)
            
    #         node = ListNode(val)
    #         tail.next = node
    #         tail = node
            
    #         l1 = l1.next if l1 else l1
    #         l2 = l2.next if l2 else l2
        
    #     return dummy.next
