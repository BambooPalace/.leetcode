#
# @lc app=leetcode id=23 lang=python
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # NO1 HARD:directly go to halfrost, recursive
        if not lists:
            return None
        n = len(lists)
        if n == 1:
            return lists[0]
        n = n // 2
        # a bit confusing here, make lists into headnodes, but how they r connected??
        left = self.mergeKLists(lists[:n])
        right = self.mergeKLists(lists[n:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2

    def mergeKListsByTwo(self, lists):
        # NO2 Garvit, after seeing VIDEO can understand ... O(nlogk)
        if not lists:
            return None
        interval = 1
        n = len(lists)
        while interval < n:
            # ??
        	for index in range(0, n - interval ,interval*2):
        		lists[index] = self.mergeTwoLists(lists[index], lists[index+interval])

        	interval *= 2

        return lists[0]





        
# @lc code=end

