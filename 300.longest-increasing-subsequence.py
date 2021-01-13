#
# @lc app=leetcode id=300 lang=python
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # no 1 WRONG idea: subsequence NOT continuous
        # sub = {}
        # seq = 1
        # sub[seq] = 1        
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[i-1]:
        #         sub[seq] += 1
        #     else:
        #         seq += 1
        #         sub[seq] = 1
        # return (sub.values())

        # no 2 WRONG, logic loopholes for cases i.e. [0,1,0,3,2,3]
        # if len(nums) == 1:
        #     return 1
        # dp = {}
        # seq = 0
        # # each seq's largest num and len
        # dp[seq] = [nums[0], 1]
        # min = nums[0]
        # for i in range(1, len(nums)):
        #     # if cur no is the smallest, add new seq
        #     if nums[i] < min:
        #         min = nums[i]
        #         seq += 1
        #         dp[seq] = [nums[i], 1]
        #     elif nums[i] == min:
        #         continue
        #     # if not, i.e. there r smaller elements then their seq len + 1
        #     else:
        #         for k in dp:
        #             if nums[i] > dp[k][0]:
        #                 dp[k][0] = nums[i]
        #                 dp[k][1] += 1
        # for k in dp:
        #     dp[k] = dp[k][1]
        # return max(dp.values())

        # no 3 xiaohao logic; O(N^2)， time beats 5%, memory beats 83%
        # if len(nums) == 1:
        #     return 1
        # dp = {}
        # # check if array saves time and the answer is NO haha
        # # dp = []
        # res = 1
        # for i in range(len(nums)):
        #     dp[i] = 1
        #     # dp.append(1)
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j]+1, dp[i])
        #             # # alternative coding
        #             # if dp[j]+1 > dp[i]:
        #             #     dp[i] = dp[j] + 1
        #     res = max(res, dp[i])
        # return res

        # no 4 halfrost sol, logic is clever and code is very tricky
        dp = []
        for num in nums:
            i = 0
            for e in dp:
                if num > e:
                    i +=1
                else:
                    break
            # if num > all numbers in dp
            if i == len(dp):
                dp.append(num)
            # update ith largest element in dp as the num
            else:
                dp[i] = num
        return len(dp)
            
        





# @lc code=end

