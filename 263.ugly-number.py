#
# @lc app=leetcode id=263 lang=python
#
# [263] Ugly Number
#

# @lc code=start
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # own, 3min
        if num == 1:
            return True
        # bug 2: 0 is special, cause infite loop
        if num <= 0:
            return False
        while num % 2 == 0:
            num /= 2
        while num % 3 ==0:
            num /= 3
        while num % 5 ==0:
            num /= 5
        return num == 1 # bug1, wrote as num==0



        


# @lc code=end

