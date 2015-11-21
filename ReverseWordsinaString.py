"""
Reverse words in a string
Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the". 

Note:
Your reversed string should not contain leading or trailing spaces.
Reduce multiple spaces to a single space in the reversed string.

"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.lstrip().rstrip()
        reverse=s.split()[::-1]
        if not reverse:
            return ''
        else:
            return ' '.join(reverse)
