"""
Add Two Numbers
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

#First solution, take two numbers, add up, then make list, not a fast solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        
        num1,num2,i,j=0,0,0,0
        while l1:
            num1=(10**i)*l1.val+num1
            l1=l1.next
            i+=1
        while l2:
            num2=(10**j)*l2.val+num2
            l2=l2.next
            j+=1
        
        num=num1+num2
        s=str(num)[::-1]
        head=ListNode(int(s[0]))
        pos=head
        for i in range(1,len(s)):
            pos.next=ListNode(int(s[i]))
            pos=pos.next
        
        return head

#Second solution,with dummy head,extra for increase in digit,and nodes to combine two list
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy=pos=ListNode(0)
        nodes=[l1,l2]
        extra=0
        while nodes or extra!=0:
            num=sum(a.val for a in nodes)+extra
            nodes=[a.next for a in nodes if a.next]
            pos.next=ListNode(num%10)
            pos=pos.next
            if num>9:
                extra=1
            else:
                extra=0
        
        return dummy.next

