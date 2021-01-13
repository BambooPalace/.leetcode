#
# @lc app=leetcode id=104 lang=python
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # NO 1 xiaohao, Recursive, DFS
        # base condition
        if root is None:
            return 0

        res = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return res

        # use STACK if not using Recursive
        
# @lc code=end

