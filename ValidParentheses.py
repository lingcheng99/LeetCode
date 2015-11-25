"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Subscribe to see which companies asked this question
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2!=0:
            return False
        stack=[]
        dict={'(':')','[':']','{':'}'}
        for i in range(0,len(s)):
            if s[i] in dict.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False
                temp=stack.pop()
                if dict[temp]!=s[i]:
                    return False
        if not stack:
            return True
        else:
            return False
