#
# @lc app=leetcode id=455 lang=python
#
# [455] Assign Cookies
#

# @lc code=start
class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        # xiaohao idea, own code 10 min
        # 在满足孩子胃口的前提下，尽可能分配小的饼干给到他
        if not s:
            return 0
        g.sort()
        s.sort()
        
        if s[0] >= g[-1]:
            return len(s)
        if s[-1] < g[0]:
            return 0
        # res = 0 # no need this, no of child iterated is the results
        child = cookie = 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:                
                child += 1
                # res += 1
            cookie += 1
        return child
            

        
# @lc code=end

