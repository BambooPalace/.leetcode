#
# @lc app=leetcode id=169 lang=python
#
# [169] Majority Element
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # own 2min, O(N) x 2, hashmap
        # n = len(nums)
        # h = {}
        # for num in nums:            
        #     if num in h:
        #         h[num] += 1
        #     else:
        #         h[num] = 1
        #     if h[num] > n//2:
        #         return num
        # # NO 2 sorting then return mid, O(NlogN), O(1)
        # nums.sort()
        # return nums[n//2]

        # no 3 O(N), O(1, boyer-moore voting
#出现次数大于总数1/2的数字只可能有一个。每次从序列里选择两个不相同的数字删除掉,
# 最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个。
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        return candidate
        
            



        
# @lc code=end

