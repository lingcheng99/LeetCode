"""
Given an integer, write a function to determine if it is a power of two. 
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n>0 and n%2==0:
            n=n/2
        return n==1
