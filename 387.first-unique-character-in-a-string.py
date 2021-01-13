#
# @lc app=leetcode id=387 lang=python
#
# [387] First Unique Character in a String
#

# @lc code=start
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        # no 1 own sol, brute force, O(n)
        # if s == '':
        #     return -1
        # # max 26 alphabets/keys
        # m = {}        
        # # one pass get counter
        # for c in s:
        #     if c in m:
        #         m[c] += 1
        #     else: 
        #         m[c] = 1
        # # check if no unique
        # hasunique = [v == 1 for v in m.values()]
        # if sum(hasunique) == 0:
        #     return -1        
        # for i, c in enumerate(s):
        #     if m[c] == 1:
        #         return i
        
        # no 2 xiaohao sol, O(2N); two pass but code cleaner
        if s == '':
            return -1 
        m = {}
        # last appear index
        for i, c in enumerate(s):
            m[c] = i
        
        # for k, v in m.items():
        for i, c in enumerate(s):
            # if 1st index == last appear index
            if m[c] == i:
                return i            
            else:
                # gist of this code
                m[c] = -1
        return -1


            

        
# @lc code=end

