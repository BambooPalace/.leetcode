#
# @lc app=leetcode id=19 lang=python
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # no 1 xiaohao, notation confusing, n-1 nodes apart, extra pre var
        # k = 0
        # res = ListNode()
        # res.next = head
        # curr = res
        # pre = ListNode()
        # # i think head is a bad notation
        # while head:
        #     head = head.next
        #     k += 1
        #     if k >= n:
        #         pre = curr
        #         curr = curr.next
                
        # pre.next = pre.next.next
        # return res.next

        # no 2 official one pass, logic clear, n nodes apart
        dummy = ListNode()
        dummy.next = head
        l = r = dummy
        
        # make n nodes apart
        for i in range(n + 1):
            r = r.next
        # both shifts right until reach end
        while r:
            l = l.next
            r = r.next
        # n nodes apart so no need extra var
        l.next = l.next.next
        return dummy.next




        
# @lc code=end

