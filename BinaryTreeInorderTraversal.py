"""
Given a binary tree, return the inorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
return [1,3,2]. 
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder=[]
        if root:
            inorder.append(root.val)
            if root.left:
                inorder=self.inorderTraversal(root.left)+inorder
            if root.right:
                inorder=inorder+self.inorderTraversal(root.right)
        return inorder
