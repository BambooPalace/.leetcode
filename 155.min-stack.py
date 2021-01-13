#
# @lc app=leetcode id=155 lang=python
#
# [155] Min Stack
#

# @lc code=start
class MinStack(object):
    # last in first out
    # 10 min draft, 15min debug, 
    # case17 still wrong, for results overflow
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')        
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min = min(self.min, x)
        

    def pop(self):
        """
        :rtype: None
        """
        # if keep poping, how to retrieve earlier min
        if self.stack:            
            self.stack.pop()
            if self.stack:
                self.min = min(self.stack)

        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

        
    def getMin(self):
        """
        :rtype: int
        """
        # require constant time so need 1 space to save the min val
        if self.stack:
            return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

