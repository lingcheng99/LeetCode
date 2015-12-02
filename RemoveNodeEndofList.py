"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.
For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass. 
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#Two-pass solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        length,pos=1,head
        while pos.next!=None:
            pos=pos.next
            length+=1
        
        if n==length:
            head=head.next
            return head
        for i in range(length-n):
            if i==0:
                p1=head
            else:
                p1=p1.next
            p2=p1.next.next
        p1.next=p2
        return head


#One-pass solution
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dic={}
        length,pos=1,head
        while pos.next!=None:
            dic[length]=pos
            length+=1
            pos=pos.next
        if length==n:
            head=head.next
            return head
        else:
            dic[length-n].next=dic[length-n].next.next
            return head
