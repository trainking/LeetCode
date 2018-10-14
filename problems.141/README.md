# Linked List Cycle

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

## 最佳解法

```
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if head == None or head.next==None:
            return False
        
        p1 = head
        p2 = head.next
        
        while(p1!=None  and p2!=None):
            if(p1==p2):
                return True
            
            p1 = p1.next
            if(p2.next==None):
                break
            if(p2.next.next==None):
                break
            p2 = p2.next.next
            
        return False
```