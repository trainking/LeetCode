# 23. 合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：

```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
```

示例 2：

```
输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]
```
 

提示：

```
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4
```

## 题解

### 堆排序法

多个数组归并排序，直接上暴力的堆排序.

### 代码示例

Python:

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        n = 0
        for item in lists:
            while item != None:
                heapq.heappush(heap, item.val)
                item = item.next
                n += 1
        del lists
        head = ListNode(None)
        g = head
        for _ in xrange(0, n):
            g.next = ListNode(heapq.heappop(heap))
            g = g.next
        return head.next
```

### 二分归并

将数组拆解为两两合并，最后归并为一个大数组，没有堆快！因为内部也是排序数组，使用堆的话，调整堆的时间并不长

### 代码示例

Python:

```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        return self.merge(lists, 0, len(lists) - 1)


    def merge(self, lists, left, right):
        if left == right: 
            return lists[left]
        mid = (left + right) // 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)


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
