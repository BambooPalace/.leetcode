#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # no 1 hash table, why if i use list instead of hashtable can't pass test case...
        # visited = {}
        
        # while head:
        #     if head in visited:
        #         return True
        #     visited[head] = 1
        #     head = head.next
        # return False

        # no 2 slow fast runner, space O(1)
        if head is None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            # two steps
            fast = fast.next.next
        return True
            
        
# @lc code=end

