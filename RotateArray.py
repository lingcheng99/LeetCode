"""
Rotate Array
Rotate an array of n elements to the right by k steps.
For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].
Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem. 
"""

#First solution with slicing
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or k==0: return
        k%=len(nums)
        temp=nums+nums[:len(nums)-k]
        nums[:]=temp[len(nums)-k:]

#Second solution, another kind of slicing
#Also slicing, shorter code
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or k==0:
            return
        k%=len(nums)
        nums[:] = nums[-k:] + nums[:-k]

#Third solution, with insert/pop
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1 or k==0:
            return
        k%=len(nums)
        for i in range(k):
            nums.insert(0,nums.pop())

