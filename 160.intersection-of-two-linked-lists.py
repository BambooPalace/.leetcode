#
# @lc app=leetcode id=160 lang=python
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # intuition 5min, draft 10min:O(m+n), stupid debug ~8min
        if not headA or not headB: 
        # bug1: headB instead of not headB, too careless
            return None

        #get end node and lenth, check if the same -> not parallel; 
        # n1 = n2 = 0
        # cur1 = headA
        # cur2 = headB
        # while cur1.next:
        #     cur1 = cur1.next
        #     n1 += 1
        # while cur2.next:
        #     cur2 = cur2.next
        #     n2 += 1
        # if cur1 != cur2:
        #     return None

        # if n1 >= n2:
        #     # set longer list head as cur 1
        #     cur1 = headA 
        #     cur2 = headB
        # else:
        #     cur1 = headB
        #     cur2 = headA
        # # use length dif to set starting point and get intersection
        # for _ in range(abs(n1-n2)):            
        #     cur1 = cur1.next

        # while cur1 and cur2:
        #     if cur1 == cur2:
        #         return cur1
        #     else:
        #         cur1 = cur1.next
        #         cur2 = cur2.next        

        #NO2 official solution, idea hard to think of, code from Garvit
        pa, pb = headA, headB
       	while pa != pb:
            # tip, `not pa else` not working, suspect due to line parsing
       		pa = pa.next if pa is not None else headB 
       		pb = pb.next if pb is not None else headA

       	return pa if pa else None
        # exit if pa == pb, or pa==pb==None both at end of list
   
# @lc code=end

