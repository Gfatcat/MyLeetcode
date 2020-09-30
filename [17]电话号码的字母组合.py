# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  示例: 
# 
#  输入："23"
# 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#  
# 
#  说明: 
# 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。 
#  Related Topics 字符串 回溯算法 
#  👍 936 👎 0

# Begin Time: 2020-09-30 10:22:53
# 执行耗时:40 ms,击败了69.93% 的Python3用户
# 内存消耗:13.4 MB,击败了35.74% 的Python3用户

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        res = []
        if digits == "":
            return res
        num_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}

        def backtrack(arr, digits):
            if len(digits) == 0:
                res.append(arr)
            else:
                for i in num_dict[digits[0]]:
                    backtrack(arr + i, digits[1:])

        backtrack('', digits)
        return res


# leetcode submit region end(Prohibit modification and deletion)


print(Solution())
