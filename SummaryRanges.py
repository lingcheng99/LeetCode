"""
Given a sorted integer array without duplicates, return the summary of its ranges.
For example, given [0,1,2,4,5,7], return ["0->2","4->5","7"]. 
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)==1:
            return [str(nums[0])]
        alist,i=[],0
        while i<len(nums):
            head=nums[i]
            if head==nums[-1]:
                alist.append(str(head))
                break
            while i<len(nums)-1 and nums[i]==nums[i+1]-1:
                i+=1
            tail=nums[i]
            if head!=tail:
                alist.append(str(head)+'->'+str(tail))
            else:
                alist.append(str(head))
            i+=1
        return alist
