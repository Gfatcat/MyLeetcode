# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法 
#  👍 635 👎 0

# Begin Time: 2020-09-30 10:34:19
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exist(self, board: List[List[str]], word: str) -> bool:
            if board == []:
                return False
            self.height = len(board)
            self.width = len(board[0])
            self.flag = False

            def backtrack(row, col, board, word):
                if self.flag == True:
                    return
                elif word == '':
                    self.flag = True
                    return
                elif row < 0 or row >= self.height or col < 0 or col >= self.width:
                    return
                if board[row][col] == word[0]:
                    temp, board[row][col] = board[row][col], '.'
                    backtrack(row - 1, col, board, word[1:])
                    backtrack(row, col - 1, board, word[1:])
                    backtrack(row + 1, col, board, word[1:])
                    backtrack(row, col + 1, board, word[1:])
                    board[row][col] = temp

            for row in range(self.height):
                for col in range(self.width):
                    if board[row][col] == word[0]:
                        backtrack(row, col, board, word)

            return self.flag


# leetcode submit region end(Prohibit modification and deletion)


print(Solution())
