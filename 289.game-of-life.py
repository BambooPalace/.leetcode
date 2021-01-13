#
# @lc app=leetcode id=289 lang=python
#
# [289] Game of Life
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # no 1 own, code 30min, brute, O(M*N) x 2
        # check against answer, logic exactly correct, but test res wrong, dont know why...
        # GOT IT: NO RETURN VALUE...modify in place
        m = len(board)
        n = len(board[0])        
        if m == 1 and n == 1:
            board[0][0] = 0
        # below method is bad as res[0][0] = 1 change cols of num
        # res = [[0] * n] * m 
        copy = [[r for r in row] for row in board]
        di = [ [a,b] for a in [-1, 0, 1] for b in [-1, 0, 1] if not (a == 0 and b == 0)]
        for i in range(m):
            for j in range(n):
                x = y = 0                
                nb = 0
                cell = copy[i][j]
                for d in di:
                    x = i + d[0]
                    y = j + d[1]
                    if x >= 0 and x < m and y >= 0 and y < n:
                        nb += copy[x][y]
                # 1 and 3
                if cell == 1 and (nb < 2 or nb > 3): # dies as default
                    board[i][j] = 0
                # elif cell == 1 and (nb == 2 or nb == 3): # keep living
                #     res[i][j] = 1 # cell
                # 4
                elif cell == 0 and nb == 3: # revive
                    board[i][j] = 1 
                # 2 and others, keep old value
                # dead cell and nb not 3 keep dead
                    

        # chanllenge, modify in place...

        
# @lc code=end

