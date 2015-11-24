"""
Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
return [3,2,1]. 
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

#Recursion code
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        postorder=[]
        if root:
            postorder.append(root.val)
            if root.right:
                postorder=self.postorderTraversal(root.right)+postorder
            if root.left:
                postorder=self.postorderTraversal(root.left)+postorder
            
        return postorder

#Iterative code
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        alist,p1,p2=[],[],[]
        p1.append(root)
        while p1:
            node=p1.pop()
            p2.append(node)
            if node.left:
                p1.append(node.left)
            if node.right:
                p1.append(node.right)
        
        while p2:
            node=p2.pop()
            alist.append(node.val)
        return alist

