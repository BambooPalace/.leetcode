#
# @lc app=leetcode id=21 lang=python
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # no1 brute force, new node, 17% time
        # head = ListNode()
        # dummy = head
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         v = l1.val 
        #         l1 = l1.next
        #     else:
        #         v = l2.val
        #         l2 = l2.next
        #     head.next = ListNode(v)
        #     head = head.next
        # head.next = l2 if l2 else l1
        # return dummy.next

        # no2 original node, update links, is it by me or inspired?
        head = ListNode()
        dummy = head
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        head.next = l1 if l1 else l2
        return dummy.next

        # no3 halfrost recursive method

        
# @lc code=end

