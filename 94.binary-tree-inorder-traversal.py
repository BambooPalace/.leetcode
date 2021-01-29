#
# @lc app=leetcode id=94 lang=python
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversalME(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # TODO try official sol see if get improvement
        # no 1 recursive, runtime top 8%
        if not root:
            return []        

        # + [] seems very slow
        return self.inorderTraversal(root.left) + [root.val] +\
        self.inorderTraversal(root.right)

    def inorderTraversal(self, root):
        # no 2 halfrost idea, OWN code FAIL
        # def helper(root, res):
        #     if not root:
        #         return res
        #     res.extend(helper(root.left, res))
        #     res.append(root.val)
        #     res.extend(helper(root.right, res))
        #     return res
        # if not root:
        #     return []
        # return helper(root, [])

        # no3 halfrost code, res is inplace, still 8%... (thought will be faster...)
        def inorder(root, res):
            if root:
                inorder(root.left, res)
                res.append(root.val)
                inorder(root.right, res)
        res = []
        inorder(root, res)
        return res



        
# @lc code=end

