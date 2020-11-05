# 21.合并两个有序列表

将两个升序链表合并为一个新的`升序`链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

```
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

## 题解

因为两个链表都是有序的，所以只要遍历比较，就可以了，可以使用递归或者迭代来实现。

### 递归

Python:

```
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2
```

### 迭代

Python:

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        dmy = ListNode(None)
        dmy.next = l1
        f = dmy
        g = l2
        while  g != None:
            while f != None:
                if f.next != None and f.next.val < g.val:
                    f = f.next
                else:
                    p = ListNode(g.val)
                    p.next = f.next
                    f.next = p
                    break
            g = g.next
        return dmy.next
```