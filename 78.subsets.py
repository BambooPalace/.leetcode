#
# @lc app=leetcode id=78 lang=python
#
# [78] Subsets
#

# @lc code=start
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """        
        # no 1 own, brute, 10 min pass! O(N*2^N) x 2
        # 2^N subsets                
        res = [[]]
        for num in nums:
            if [num] not in res: #(2^N)
                for r in res[1:]:
                    if num not in r:
                        # take up memory... (N)
                        temp = r[:]
                        temp.append(num)
                        # alternative line: temp += num
                        res.append(temp)   
                                                             
                res.append([num])
                # alternative line: res += [[num]]
        return res

        # NO2 Garvit
        result = [[]]
        for num in nums:
        	for j in range(len(result)):
        		result.append(result[j] + [num])
        return result
        
        # to check official solutions
                


        
# @lc code=end

