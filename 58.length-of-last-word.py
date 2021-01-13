#
# @lc app=leetcode id=58 lang=python
#
# [58] Length of Last Word
#

# @lc code=start
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # # no 1 brute force strip spaces at the end
        # if s == '':
        #     return 0
        # # if s = '    '
        # while s != '' and s[-1] == ' ':
        #     s = s[:-1]
        # if s == '':
        #     return 0

        # for i in range(1, len(s)+1):
        #     if s[-i] == ' ':
        #         return i - 1
        # return len(s)

        #no 2 python function
        # words = s.strip(' ').split(' ')
        # return len(words[-1])

        # no 3 improve no 1
        if s == '':
            return 0
        n = len(s)
        c = 0
        for i in range(1, n+1):
            if s[-i] != ' ':
                c += 1
            if c > 0 and s[-i] == ' ':
                return c
        
        return c


        
# @lc code=end

