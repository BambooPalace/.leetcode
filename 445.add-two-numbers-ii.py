#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # no 1 use integer
        # x1, x2 = 0, 0
        # while l1:
        #     x1 = x1*10 + l1.val
        #     l1 = l1.next
        # while l2:
        #     x2 = x2*10 + l2.val
        #     l2 = l2.next
        # s = x1 + x2

        # head = ListNode()
        # if s == 0:
        #     return head
        # curr = head

        # while s:            
        #     ### confused how to add node backwards
        # return head.next

        # no 2 stack
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        s = 0
        # this node is at the end??
        list = ListNode()
        while s1 or s2:
            if s1:
                s += s1.pop()
            if s2:
                s += s2.pop()
            list.val = s % 10
            s /= 10
            head = ListNode(s)
            head.next = list
            list = head
        if list.val == 0:
            return list.next
        return list


# @lc code=end

