# 24. 两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

**你不能只是单纯的改变节点内部的值**，而是需要实际的进行节点交换。

## 题解

增加一个空头节点，然后两两交换时，有一个指针指向这二者的前驱节点

### 代码示例

Python:

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        prev = dom = ListNode(None)
        dom.next = head
        while prev.next != None and prev.next.next !=None:
            first,second = prev.next,prev.next.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dom.next
```
