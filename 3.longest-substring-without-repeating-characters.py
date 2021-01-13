#
# @lc app=leetcode id=3 lang=python
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # confused about sliding window...seem easy but cant code correctly
        # 2nd time visit, can understand better

        # no1, skip xiaohao for now

        # NO 2, garvit, FAST 90%, 40ms; sliding window, if right of window has repeating letter, move left to rightmost idx of this letter
        # n = len(s)
        # if n <= 1:
        #     return n
        # start = res = 0
        # set = {}
        # for end in range(n):
        #     if s[end] in set:
        #         start = max(set[s[end]], start)
        #     res = max(res, end - start + 1)
        #     set[s[end]] = end + 1 # record letter's next idx, update if repeated
        # return res

        # NO3 halfrost, two pointers, code NOT nicely done,top 40%
# 滑动窗口的右边界不断的右移，只要没有重复的字符，就持续向右扩大窗口边界。一旦出现了重复字符，
# 就需要缩小左边界，直到重复的字符移出了左边界，然后继续移动滑动窗口的右边界。
# 以此类推，每次移动需要计算当前长度，并判断是否需要更新最大长度，最终最大的值就是题目中的所求。
        # if not s:
        #     return 0
        # res, left, right = 0, 0, -1
        # freq = {}
        # while left < len(s) and right < len(s)-1:            
        #     if (s[right+1] not in freq or freq[s[right+1]]==0):
        #         freq[s[right+1]] = 1
        #         right += 1
        #     else:
        #         freq[s[left]] -= 1
        #         left += 1
        #     res = max(res, right-left+1)
        # return res

        # NO4 NEETCODE, 6min explanation, 56ms, top 57%
        set_ = set() # keep unique letters in the window
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in set_:
                set_.remove(s[l])
                l += 1
            set_.add(s[r])
            res = max(res, r-l+1)
        return res


        
# @lc code=end

