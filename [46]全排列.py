# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法 
#  👍 928 👎 0

# Begin Time: 2020-09-30 10:26:03
# 执行耗时:60 ms,击败了6.15% 的Python3用户
# 内存消耗:13.4 MB,击败了76.06% 的Python3用户
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def backtrack(self, arr, pos, end):
        if pos == end:
            self.ans.append(arr[:])
        else:
            for i in range(pos, end):
                arr[pos], arr[i] = arr[i], arr[pos]
                self.backtrack(arr, pos + 1, end)
                arr[pos], arr[i] = arr[i], arr[pos]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(nums, 0, len(nums))
        return self.ans


# leetcode submit region end(Prohibit modification and deletion)


print(Solution())
