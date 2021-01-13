#
# @lc app=leetcode id=88 lang=python
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """        
        
        # no 1: after 7 min, no idea, halfrost idea and own code, not right...
        # if m == 0:
        #     nums1 = nums2
        #     return None # this line is for easy exit
        
        # WRONG...but how to make it right?
        # for k in range(m+n-1, -1, -1):
        #     i, j = m - 1, n - 1
        #     while i >= 0 and j >= 0:                    
        #         if nums1[i] > nums2[i]:
        #             nums1[k] = nums1[i]
        #             i -= 1
        #         else:
        #             nums1[k] = nums2[j]
        #             j -= 1
        #     # if nums2 done, no need to furthur update nums1
        #     while i < 0 and j >= 0:
        #         nums1[k] = nums2[j]
        #         j -= 1
            
        
        # no 2halfrost sol: iterate from right to left
        if m == 0:
            # nums1 = nums2 cannot replace in place, wierd
            nums1[:] = nums2            
            return None
        i = m - 1
        j = n - 1
        k = m + n -1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
            

        

                
        
# @lc code=end

