#
# @lc app=leetcode id=82 lang=python
#
# [82] Remove Duplicates from Sorted List II
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
        # compelx... draft time 13min, #debug 30min; my idea is good, same as halfrost no 4, 
        # coding skill is not good, very tricky to set conditions  
        res = temp = ListNode(val=101)
        res.next = head
        pre = res                
        while head and head.next: # include [] case
            if head.val == temp.val:
                # remove head, keep pre
                pre.next = head.next                
                head = head.next                             
            elif head.val == head.next.val:                                            
                pre.next = head.next.next
                temp = head
                head = head.next.next
            else: # otherwise goes to next node
                pre = head
                head = head.next
        # bug 1: wrong for [1,1,1], get stuck, find instincts from halfrost, need check final element; 
        # bug 2: temp.val>0; not temp; default temp with val 0; 因为不严谨都错了。。。can add a boolean variable to simplify things
        if head and head.val == temp.val:
                # remove head, keep pre
                pre.next = None # aka, None                                

        return res.next # empty node is use when orig head node might be removed
        
        
# @lc code=end

