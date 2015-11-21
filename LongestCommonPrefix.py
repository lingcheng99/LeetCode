"""
Write a function to find the longest common prefix string amongst an array of strings. 
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs==[]:
            return ''
        if len(strs)==1:
            return strs[0]
        minlength=len(min(strs,key=len))
        i=0
        while i<minlength:
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    break
            if strs[j][i]==strs[0][i]:
                i+=1
            else:
                break
        return strs[0][:i]
