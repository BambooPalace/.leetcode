#
# @lc app=leetcode id=238 lang=python
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Own without division, brute; O(N^2), O(N). TLE        
        # n = len(nums) # given n > 1
        # res = [1] * n
        # for i in range(n):
        #     for j in range(n):
        #         if i == j:
        #             continue
        #         else:
        #             res[j] *= nums[i]
        # return res

        # NO1, official sol 1; O(N) x 2, dont understand well
        # check TECH DOSE, video much easier to understand, res equals to product of left and right
        # many bugs in tiny places...TAT
        
        # n = len(nums)
        # left, right, product = [1]*n, [1]*n, [1]*n
        # for i in range(1, n):
        #     left[i] = left[i-1] * nums[i-1]
        # # tip: code backward is better, as it s intuitive and less likely to make mistakes
        # for i in range(n-2, -1, -1): 
        #     # bug1, range(1,n) confusing, and wrong idx...used i,j,k initially
        #     right[i] = right[i+1] * nums[i+1]
        # for i in range(n):
        #     product[i] = left[i] * right[i]
        # return product

        # NO2 inplace O(N), O(1), save right as a temp variable instead of a list
        n = len(nums)
        left, right = [1]*n, 1
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        for i in range(n-1, -1, -1):
            left[i] = right * left[i]
            right *= nums[i]
        return left
        




        
# @lc code=end

