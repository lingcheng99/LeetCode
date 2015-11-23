
"""
Reverse a singly linked list
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
         
class Solution:
    def reverseList(self,head):
        if not head:
            return
        reverse=None
        while head:
            current=head
            head=head.next
            current.next=reverse
            reverse=current
        return reverse
