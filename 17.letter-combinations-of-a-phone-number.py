#
# @lc app=leetcode id=17 lang=python
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if not digits:
            return []
        # NO 1 leetcode Sol directly, backtrack       
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])                    
        output = []
        if digits:
            backtrack("", digits)
        return output

        # NO2 own, iterative, memory exceed.. why?? 
        # maybe coz i add res in place then for loop in res never ends   
        # res = ['']
        # for d in digits:
        #     # add below line inspired by garvit
        #     temp = []
        #     for r in res:
        #         for l in phone[d]:                
        #             temp.append(r + l)
        #     res = temp
        # return res

        # NO 3: Garvit
        res = ['']
        for d in digits:
            letters = phone[d]
            new_res = []
            for prefix in res:                
                for l in letters:
                    new_res.append(prefix + l)
            res = new_res
            # res = [prefix+l for l in letters for prefix in res]
        return res



        
# @lc code=end

