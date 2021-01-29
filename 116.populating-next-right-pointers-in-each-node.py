#
# @lc app=leetcode id=116 lang=python
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # time top 5%, why so slow...labu code
        def connectTwo(left, right):
            if not left or not right:
                return None
            left.next = right
            # default next val is null, no need extra line

            connectTwo(left.left, left.right)
            connectTwo(right.left, right.right)
            connectTwo(left.right, right.left)

        if not root:
            return None            
        connectTwo(root.left, root.right)
        return root
    
    # garvit solution wrong, halfrost no sol


        
# @lc code=end

