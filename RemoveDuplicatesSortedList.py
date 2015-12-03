"""
Remove Duplicates from Sorted List
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3. 
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        while head and head.next and head.val==head.next.val:
            head=head.next
        pos=head
        while pos and pos.next:
            if pos.val==pos.next.val:
                pos.next=pos.next.next
            else:
                pos=pos.next
        return head
        


