#
# @lc app=leetcode id=16 lang=python
#
# [16] 3Sum Closest
#

# @lc code=start
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # no memory, try modify based on 3Sum
        # code NOT nice, FAIL [-100,-98,-2,-1]

        # n=len(nums)
        # res=[]
        # if(not nums or n<3):
        #     return []
        # nums.sort()
        # diff = float('inf') 
        # for i in range(n):
        #     if i>0 and nums[i]>target:
        #         break
        #     if(i>0 and nums[i]==nums[i-1]):
        #         continue
        #     L=i+1
        #     R=n-1
        #     while(L<R):
        #         temp = nums[i]+nums[L]+nums[R] - target
        #         if temp == 0 :
        #             return target
        #         elif temp > 0:
        #             R=R-1
        #             diff = diff if abs(diff) < temp else temp
        #         else:
        #             L=L+1
        #         # bug, how to include sign
        #             diff = diff if abs(diff) < -temp else temp
        # return target + diff

        # # NO2 official, tricky, simple code. SHOULD type over by myself
        diff = float('inf')
        nums.sort()
        for i in range(len(nums)):
            lo, hi = i + 1, len(nums) - 1
            while (lo < hi):
                sum = nums[i] + nums[lo] + nums[hi]
                # trick, include diff in if condition
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break
        return target - diff
        
# @lc code=end

