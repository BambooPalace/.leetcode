#
# @lc app=leetcode id=110 lang=python
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
    
        # try own code, fail. This is not easy...
        # def depth(root, res=0):
        #     if not root:
        #         res += 0
        #         return res                
        #     if not root.left or not root.right:
        #         res += 1
        #         return res
      
        #     return max(depth(root.left, res), depth(root.right, res))
        
        # if not root:
        #     return True        
        # return abs(depth(root.left) - depth(root.right)) <= 1

        # NO 2 , modified based on xiaohao
        # bug 1: wrong depth function
        def depth(root):
            if not root:
                return 0
            # at least depth = 1             
            return max(depth(root.left), depth(root.right)) + 1
        
        if not root:
            return True        
        # bug 2: for [1,2,2,3,null,null,3,4,null,null,4] not a balanced true
        # so add below line
        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        return abs(depth(root.left) - depth(root.right)) <= 1
                
# @lc code=end

