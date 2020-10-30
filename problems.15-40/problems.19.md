# 19.删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第`n`个节点，并且返回链表的头结点。

示例：

给定一个链表:`1->2->3->4->5`, 和`n = 2`.

当删除了倒数第二个节点后，链表变为`1->2->3->5`.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

## 题解

### 双指针协同步骤法

题中指示的是删除**倒数**第几个节点，因此，我们可以准备两个指针，开始都指向头节点，后一个指针，先走要删除的位置步数，然后两个指针再协同步骤，直到，先走指针到了末尾，则删除第一个指针的数据。

#### 代码示例

Python：

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = head  # 后走
        slow = head  # 先走
        for _ in range(0, n):
            slow = slow.next
        if slow == None:
            head = head.next
            return head
        while slow != None:
            if slow.next == None:
                first.next = first.next.next
            slow=slow.next
            first = first.next
        return head
```

### 栈弹出法

建立一个栈，然后利用栈的先入后出特性，弹出元素，最后在栈顶的就是要删除的前驱节点。

#### 代码示例

Python:

```
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cur = dummy
        while cur:
            stack.append(cur)
            cur = cur.next
        
        for i in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next
        return dummy.next
```