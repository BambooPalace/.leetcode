#
# @lc app=leetcode id=112 lang=python
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        # own 10 mins, fail, reason maybe res is private parameter
        if not root:
            return False
        val = root.val

        def checkSum(root, res=val):
            if not root:
                return False
            res += root.val
            if not root.left and not root.right:                
                return sum == root.val
            # fix 1: still wrong...
            return checkSum(root.left, res) or checkSum(root.left, res)
            # checkSum(root.left, res)
            # checkSum(root.right, res)                
        return checkSum(root.left) or checkSum(root.right)

        #  NO2 cant debug on my own, based on halfrost
        if not root:
                return False
        if not root.left and not root.right:                
            return sum == root.val        
        
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)


# @lc code=end

