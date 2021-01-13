#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # # no 1: Garvit
        if not head:
        	return None

        slow = fast = head
        # below line cause over time limit....why???
        # slow, fast = head, head.next

        while fast and fast.next:
        	slow = slow.next
        	fast = fast.next.next
        	if slow == fast:
        		break

        if slow == fast:
        	slow = head
        	while slow != fast:
        		slow = slow.next
        		fast = fast.next
        	return slow
        return None

        # # no 2: jiuzhuang
        # if head == None or head.next == None:
        #     return None
        # slow = fast = head  		#初始化快指针和慢指针
        # while fast and fast.next:	
        #     slow = slow.next
        #     fast = fast.next.next
        #     if fast == slow:		#快慢指针相遇
        #         break
        # if slow == fast:
        #     slow = head				#从头移动慢指针
        #     while slow != fast:
        #         slow = slow.next
        #         fast = fast.next
        #     return slow				#两指针相遇处即为环的入口
        # return None
        
# @lc code=end

