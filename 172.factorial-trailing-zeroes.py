#
# @lc app=leetcode id=172 lang=python
#
# [172] Factorial Trailing Zeroes
#

# @lc code=start
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # simple but tricky
        # NO 1 own 7min, TLE for n=6445...log(N)
        # fact = 1
        # for i in range(1, n+1):
        #     fact *= i        
        # res = 0
        # while fact % 10 == 0:
        #     res += 1
        #     fact = fact // 10 + (fact % 10)
        # return res

        # NO2, halfrost, O(logN);
        #res = N/5 + N/(5^2) + N/(5^3) + ... = ((N / 5) / 5) / 5 /...
        # if n//5 == 0:
        #     return 0
        # return n//5 + self.trailingZeroes(n//5)

        # NO3 modify no2 to iterative, cant on my own. copy leetcode discuss
        #find how many number can be dived by 5, 5*5 ... and sum up.
        res = 0
        while n > 0:
            n /= 5
            res += n
        return res

        





        
# @lc code=end

