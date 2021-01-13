#
# @lc app=leetcode id=206 lang=python
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # no 1 iterative 想不明白及时看答案
        # pre = None
        # curr = head
        # while curr:
        #     # save temp val
        #     next = curr.next
        #     # reverse arrow
        #     curr.next = pre
        #     # shift pre and curr node to right
        #     pre = curr
        #     curr = next
            
        #     # no arrow between pre to curr now
        # return pre

        # no 2 recursive, a bit obscure
        if head is None or head.next is None:
            return head
        p = reverseList(head.next)
        head.next.next = head
        head.next = None
        return p


# @lc code=end

