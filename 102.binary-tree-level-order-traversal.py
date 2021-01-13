#
# @lc app=leetcode id=102 lang=python
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        # xiaohao DFS, DIFFICULT, cant think of on my own
        def dfs(root, level, res):
            if not root:
                return res
            if len(res) == level:
                res.append([root.val])
            else:
                res[level].append(root.val)
            
            res = dfs(root.left, level+1, res)
            res = dfs(root.right, level+1, res)
            return res
        
        return dfs(root, 0, [[]])

        # NO2  to check BFS by Garvit, halfrost

        
# @lc code=end

