#
# @lc app=leetcode id=108 lang=python
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # own 15 mins, TLE...
        if not nums:
            return None        
        mid = (len(nums)-1)//2
        # no need two pointers...as l is always 0 and r len-1        
        root = TreeNode(val = nums[mid])
        # bug 1, recursive no need while loop, thus TLE
        # wrong code : while l <= r:                     
        root.left = self.sortedArrayToBST(nums[:mid])        
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

        # runtime slow even when my sol passes
 


        
# @lc code=end

