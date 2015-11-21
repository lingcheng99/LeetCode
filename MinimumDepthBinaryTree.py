"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1

        min_left = self.minDepth(root.left)
        min_right = self.minDepth(root.right)
        min_depth = min(min_left,min_right) + 1
        return min_depth
