#
# @lc app=leetcode id=18 lang=python
#
# [18] 4Sum
#

# @lc code=start
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # own, reuse three sum, code 10 min, debug 10min FAIL
        # BUG: return [], threeSum function is wrong... why????
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        for i in range(n):
            if nums[i] > target/4 :
                return []
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # bug2: new target is 'target - nums[i]', stupid...
            three = self.threeSum(nums[i+1:], target-nums[i])
            if three: # bug1: wrote 'no three'
                # bug3: append return None
                # three = [ [nums[i]] + t for t in three]
                # res += three      
                for t in three:
                    t.append(nums[i])
                    res.append(t)      
        return res

    # NO2 Garvit- hashset?, halfrost code long...
    
    # NO3 official, Ksum
        def kSum(nums, target, k):
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i - 1] != nums[i]:
                    for _, set in enumerate(kSum(nums[i + 1:], target - nums[i], k - 1)):
                        res.append([nums[i]] + set)
            return res

        def twoSum(nums, target):
            res = []
            lo, hi = 0, len(nums) - 1
            while (lo < hi):
                sum = nums[lo] + nums[hi]
                if sum < target or (lo > 0 and nums[lo] == nums[lo - 1]):
                    lo += 1
                elif sum > target or (hi < len(nums) - 1 and nums[hi] == nums[hi + 1]):
                    hi -= 1
                else:
                    res.append([nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
            return res

        # nums.sort()
        # return kSum(nums, target, 4)


    def threeSum(self, nums, target): 
        # from xiaohao, 792ms, top 49%, O(N)
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        # nums.sort()
        res=[]
        for i in range(n):
            if(nums[i]>target):
                return res
            # 4Sum bug, modify 0 as target
            if(i>0 and nums[i]==nums[i-1]):
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==target):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]>target):
                    R=R-1
                else:
                    L=L+1
        return res
        
# @lc code=end

