"""
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree: 
   1
 /   \
2     3
 \
  5
All root-to-leaf paths are: 
["1->2->5", "1->3"]
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        paths=[]
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        if root.left:
            paths+=[str(root.val)+'->'+child for child in self.binaryTreePaths(root.left)]
        if root.right:
            paths+=[str(root.val)+'->'+child for child in self.binaryTreePaths(root.right)]
        return paths
