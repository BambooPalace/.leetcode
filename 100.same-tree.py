#
# @lc app=leetcode id=100 lang=python
#
# [100] Same Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # own, ~20min, idea right + bug fix
        if not p and not q:
            return True
        # when one is None and the other is NOT + 1fix
        if (p and not q) or (q and not p):
            return False
        # both not None
        if p.val != q.val: 
            return False                
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        # NO2 halfrost same idea diff code
        if not p and not q:
            return True
        if p and q:
            if p.val != q.val: 
                return False                            
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# @lc code=end

