#
# @lc app=leetcode id=4 lang=python
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float                
        """
        # no 1 try 17min, realise not as easy and straightforward as i thought    
        if not nums1 and not nums2:
            return None

        m = len(nums1)
        n = len(nums2)

        # add code for if one list is empty
        # if write edge cases for below code is too messy
        # if nums1[-1] <= nums2[0]:
        #     if (m+n) % 2 > 0:
        #         if m > n:
        #             return nums1[(m+n)//2 + 1]
        #         else:
        #             return nums2[(m+n)//2 - m]

        # no2 brute force, O(m+n), spent 1hr to modify my conditions and debug

        res = []
        count = (m + n)//2 +1   
        i = j = c = 0     
        if not nums1:
            res = nums2
            c = n
        elif not nums2:
            res = nums1
            c = m
        elif nums2[-1] <= nums1[0]:
            res = nums2
            c = n
            j = n
        elif nums1[-1] < nums2[0]:
            res = nums1
            c = m
            i = m                       
                
        while c < count and i <= m and j <= n:
            # if i == m and j == n, then c must over count ard
            if i == m and j < n:
                res.append(nums2[j])        
                j += 1
            elif j == n and i < m:
                res.append(nums1[i])
                i += 1
            elif nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else: 
                res.append(nums2[j])
                j += 1
            c += 1
        # return res
        if (m+n) % 2 > 0:
            return res[count-1] # idx = num - 1
        else:
            # ... if use / 2 return integer instead of float...  
            return (res[count-1] + res[count-2]) / 2.0
        
        # no 3, binary search, not study this yet

        

        
# @lc code=end

