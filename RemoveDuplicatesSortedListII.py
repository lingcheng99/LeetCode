"""
Remove Duplicates from Sorted List II
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 
"""
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#First solution, in-place
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        while head and head.next and head.val==head.next.val:
            temp=head.val
            changed=False
            while head.next and head.next.val==temp:
                head=head.next
                changed=True
            if changed and head and head.val==temp:
                head=head.next
                    
        if head and head.next:
            p1,p2=head,head.next
        else:
            return head
            
        while p1 and p2 and p2.next:
            changed=False
            while p2.val==p2.next.val:
                temp=p2.val
                changed=True
                p2=p2.next
                p1.next=p2.next
                p2=p2.next
                if not p2:
                    return head
                if not p2.next:
                    if p2.val==temp:
                        p1.next=None
                        return head
                    else:
                        return head
            if changed:
                if p2.val==temp:
                    p1.next=p2.next
                    p2=p2.next
            else:
                p1=p1.next
                p2=p2.next
        return head

#Second solution, with dummy head
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pos=dummy
        dval=None
        while head:
            if head.next and head.val==head.next.val:
                dval=head.val
            if dval==None or head.val!=dval:
                pos.next=head
                pos=pos.next
            head=head.next
        pos.next=None
        return dummy.next
