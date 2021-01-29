#
# @lc app=leetcode id=114 lang=python
#
# [114] Flatten Binary Tree to Linked List
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
	# labu code
        if not root:
            return None
        # post order traversal
        self.flatten(root.left)
        self.flatten(root.right)

        # flatten a subtree of parent node
        right = root.right
        root.right = root.left
        root.left = None
        
        # find last node of the flattened left node, 
        # link to first node of the flatten right node

        # BUG1, not consider if right node is None
        # cur = root.right         
        # while cur.right:
        #     cur = cur.right
        # cur.right = right

        # FIX1
        while root.right:
            root = root.right
        root.right = right


        
# @lc code=end

