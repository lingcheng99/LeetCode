"""
Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
return [1,2,3]. 
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
         
#Recursion code
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preorder=[]
        if root:
            preorder.append(root.val)
            if root.left:
                preorder+=self.preorderTraversal(root.left)
            if root.right:
                preorder+=self.preorderTraversal(root.right)
        
        return preorder
        
#Iterative code
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack=[root]
        alist=[]
        while stack:
            node=stack.pop()
            alist.append(node.val)
            if node.right:
                stack+=[node.right]
            if node.left:
                stack+=[node.left]
        return alist
