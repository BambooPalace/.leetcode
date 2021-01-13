#
# @lc app=leetcode id=107 lang=python
#
# [107] Binary Tree Level Order Traversal II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """  
        # TREE Traversal difficult for me TAT      
        # NO1 own 14 min, FAIL massively...(if not confident, should also check solution early)
        def bfs_bug(root, res = [[]], level = 0):
            if not root:
                return res
            if not root.left and not root.right:
                if not res[level]:
                    res.append([])
                    level += 1 # wrong for else condition
                res[level].append(root.val)     
            res += bfs(root.left, res, level) # NOT +=
            res += bfs(root.right, res, level)
            return res  
        # modify dfs based on xiaohao, top to bottom
        def bfs(root, res = [[]], level = 0):
            if not root:
                return res            
            if len(res) == level:
                res.append([])                
            res[level].append(root.val)     
            res = bfs(root.left, res, level+1)
            res = bfs(root.right, res, level+1)
            return res  
       

        # NO2, leetcode discuss, confusing     

        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, root, level, res):
        if root:
            if len(res) < level + 1:
                res.insert(0, [])
            res[-(level+1)].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)

             
                
                    


# @lc code=end

