"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.maxDepth(root.right)+1
        if not root.right:
            return self.maxDepth(root.left)+1

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        max_depth = max(max_left,max_right) + 1
        return max_depth
