"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character but a character may map to itself.
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        dict1,dict2={},{}
        for i in range(len(s)):
            if dict1.has_key(s[i]):
                if dict1[s[i]]!=t[i]:
                    return False
            else:
                dict1[s[i]]=t[i]
            if dict2.has_key(t[i]):
                if dict2[t[i]]!=s[i]:
                    return False
            else:
                dict2[t[i]]=s[i]
        return sorted(dict1.keys())==sorted(dict2.values())
