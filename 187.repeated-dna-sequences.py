#
# @lc app=leetcode id=187 lang=python
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # halfrost hashmap
        if len(s) < 10:
            return []
        res = []
        h = {}        
        for i in range(len(s) - 9):
            seq = s[i:i+10]            
            if seq not in h:
                h[seq] = 1
            elif h[seq] == 1:
                res.append(seq)
                h[seq] += 1
        return res

        # another solution is bit 
        
# @lc code=end

