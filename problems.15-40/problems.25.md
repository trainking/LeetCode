# 25. K 个一组翻转链表


给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

**示例：**

```
给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5
```
 

说明：

你的算法只能使用常数的额外空间。
**你不能只是单纯的改变节点内部的值**，而是需要实际进行节点交换。

## 题解

与交换节点同理，一个前驱节点指针，然后找出需要倒转的节点，倒转之后，前驱节点指针正好再次指向**子链表**的头。

### 代码示例

Python:

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dom = ListNode(-1)
        dom.next = head   # 头，子链表交换头
        prev = dom   # 前驱指针
        while head != None:
            n = []
            t = head
            for _ in xrange(0, k):
                if t != None:
                    n.append(t)
                    t= t.next
                else:
                    break
            l_n = len(n)
            if l_n < k:
                return dom.next
            prev.next = self.reverse(head, n, l_n, k)
            # 翻转之后头就是前驱节点
            prev = head
            head = head.next
        return dom.next

    def reverse(self, head, n, l_n, k):
        _last = n[-1].next
        for g in xrange(1, l_n):
            n[-g].next = n[-g-1]
        n[0].next = _last
        return n[-1]
```
