#
# @lc app=leetcode id=83 lang=python
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # have done this before, cant remember tho, 10 min write 10 min debug        
        dummy = head        
        # stop before last node, so that below if condition can run
        while head and head.next: # add `head and` can handle [] case
            if head.val == head.next.val:                               
                head.next = head.next.next
            else:# bug 1, wrong logic
                head = head.next
        return dummy



        
# @lc code=end

