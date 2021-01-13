#
# @lc app=leetcode id=101 lang=python
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # NO1 own 5min, but wrong idea
        # if not root:
        #     return True
        # if root.left and root.right:
        #     if root.left.val != root.right.val:
        #         return False
        #     # wrong idea...
        #     return self.isSymmetric(root.left) and self.isSymmetric(root.right)
        # else: # if one is None and the other is not
        #     return False

        # NO2 idea traverse subtree left to right, and righ to left
        # cant code coz its a BAD IDEA
        # if not root:
        #     return True        
        # if root.left and root.right:
        #     return bds(root.left) == bfs(root.right)
        # else:
        #     return False
        
        # NO3 halfrost idea: invert subtree and check if same
        

        # NO4 official, GOOD IDEA
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            # pretty tricky idea
            return t1.val==t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

        return isMirror(root, root)


        
# @lc code=end

