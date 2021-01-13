#
# @lc app=leetcode id=98 lang=python
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # xiaohao idea and my code adaption, got def wrong...
        # fail this: [5,4,6,null,null,3,7] coz all right subtree need to larger
        
        # if not root or (not root.left and not root.right):
        #     return True
        # if root.right and root.right.val <= root.val:
        #     return False
        # if root.left and root.left.val >= root.val:
        #     return False                       
        
        # return self.isValidBST(root.left) and self.isValidBST(root.right)

        # NO 2 , official solution, TO UNDERSTAND
        def validate(node, low=-float('inf'), high=float('inf')):
            # Empty trees are valid BSTs.
            if not node:
                return True
            # The current node's value must be between low and high.
            if node.val <= low or node.val >= high:
                return False
            
            # The left and right subtree must also be valid.
            return (validate(node.right, node.val, high) and
                   validate(node.left, low, node.val))
        
        return validate(root)
        
        
# @lc code=end

