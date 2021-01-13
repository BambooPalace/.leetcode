#
# @lc app=leetcode id=15 lang=python
#
# [15] 3Sum
#

# @lc code=start
class Solution(object):
    def MYthreeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # by memory 10 min, TLE? stuck in while loop
        # top 5%, need better duplicates handling to be faster 
        n = len(nums)
        if n < 3:
            return []
        res = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break            
            l = i + 1
            r = n - 1
            while l < r:
                # use of lists makes slightly slower
                three = [nums[i], nums[l], nums[r]]
                if sum(three) == 0:
                    if three not in res:
                        res.append(three)
                    # bug1: forgot below lines, stuck in while loop
                    r -= 1
                    l += 1
                elif sum(three) > 0:
                    r -= 1
                else:
                    l += 1
        return res

    def threeSum(self, nums): 
        # from xiaohao, 792ms, top 49%
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>0):
                return res
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>0):
                    R=R-1
                else:
                    L=L+1
        return res
            


        
# @lc code=end

