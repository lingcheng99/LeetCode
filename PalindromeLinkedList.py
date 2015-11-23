"""
Given a singly linked list, determine if it is a palindrome.
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        reverse = []
        while head:
            reverse.append(head.val)
            head = head.next
        return reverse == reverse[::-1]
