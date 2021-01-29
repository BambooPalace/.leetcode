#
# @lc app=leetcode id=79 lang=python
#
# [79] Word Search
#

# @lc code=start
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # seem difficult, go straight to solution, still hate backtracking, understand None
        # NO1 Garvit, DFS more common approach, O(m*n*4**l): dfs worst is O(4**l), O(1)? O(m+n)
        m = len(board)
        n = len(board[0])
        res = False
        for row in range(m):
            for col in range(n):
                if self.dfs(board, word, row, col, 0):
                    return True
        return False
    
    def dfs(self, board, word, row, col, depth):        
        if row < 0 or col < 0 or row >= len(board) or col>= len(board[0]):
            return False
        # what is current length?
        if board[row][col] == word[depth]:
            c = board[row][col]
            board[row][col] = '#' #??
            if depth == len(word) - 1:
                return True
            # 4 directions
            elif self.dfs(board, word, row-1, col, depth+1)\
                or self.dfs(board, word, row+1, col, depth+1)\
                or self.dfs(board, word, row, col-1, depth+1)\
                or self.dfs(board, word, row, col+1, depth+1):
                return True
            board[row][col] = c

        # NO2 halfrost, 在地图上的任意一个起点开始，向 4 个方向分别 DFS 搜索，
        # 直到所有的单词字母都找到了就输出 true，否则输出 false。
        dirs = [[-1,0], [0,1], [1,0], [0,-1]]
        visited = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                v = board[i][j]
                if search(board, vissited, word, 0, i, j):
                    return True
        return False

        def inboard(board, visited, word, index, x, y):
            return x>=0 and x < len(board) and y >= 0 and y < len(board[0]):
        def search(board, visited, word, index, x, y):
            if index == len(word-1):
                return board[x][y] == word[index]
            if board[x][y] == word[index]:
                visited[x][y] = True
            for dir in dirs:
                nx = x + dir[0]
                ny = y + dir[1]
                if isInBoard(board, nx, ny) and not visited[nx][ny] \
                    and searchWord(board, visited, word, index+1, nx, ny):
                    return True
			visited[x][y] = False
            return False
            




        
# @lc code=end

