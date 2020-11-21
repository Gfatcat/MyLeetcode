# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。 
# 
#  '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
#  
# 
#  所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
#  
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
#  
# 
#  示例 5: 
# 
#  输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false 
#  Related Topics 字符串 动态规划 回溯算法 
#  👍 1599 👎 0

# Begin Time: 2020-10-09 18:10:54
# 解答成功:
# 执行耗时:52 ms,击败了93.28% 的Python3用户
# 内存消耗:13.2 MB,击败了95.04% 的Python3用户
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # region 递归
    def isMatch(self, s: str, p: str) -> bool:
        if not p:  # 结束条件
            return not s

        self.cache = {}  # 记录处理过的(s-p)对
        self.build(s, p)  # 构建缓存
        return self.cache[(s, p)]

    def build(self, s, p):
        if not p:  # 结束条件
            return not s

        # 查缓存
        if (s, p) in self.cache:
            return self.cache[(s, p)]

        first_match = (len(s) > 0) and p[0] in {s[0], '.'}

        # 先处理 `*`
        if len(p) >= 2 and p[1] == '*':
            # 匹配0个或多个
            result = self.build(s, p[2:]) or (first_match and self.build(s[1:], p))
        else:
            # 处理 s[0]或`.` ，匹配一个
            result = first_match and self.build(s[1:], p[1:])

        self.cache[(s, p)] = result
        return result
    # endregion

    # region 动态规划
    # 状态 dp[i][j]=>s[i]与p[j]的匹配状态
    # 状态转移 dp[i-1][j-1]
    # p[j]是一个字母: s[i]==p[j] => dp[i][j] = dp[i-1][j-1]
    # p[j]=='.': dp[i][j] = dp[i-1][j-1]
    # p[j]=='*': 三种情况或
    #   1) 匹配零个: s[i]!=p[j-1] => dp[i][j] = dp[i][j-2]
    #   2) 匹配一个: s[i]==p[j-1] or p[j-1] == '.' => dp[i][j] = dp[i][j-1]
    #   2) 匹配多个: s[i]==p[j-1] or p[j-1] == '.' => dp[i][j] = dp[i-1][j]
    #   2) p[j-1]是一个
    # def isMatch(self, s: str, p: str) -> bool:
    #     dp = [[False for i in range(len(s))] for j in range(len(p))]
    #     s_index = 1
    #     p_index = 1
    #     if p[0] == '.' or s[0] == p[0]:
    #         dp[0][0] = True
    #     while s_index < len(s) and p_index < len(p):
    #         if p[p_index] == '.' or s[s_index] == p[p_index]:
    #             dp[s_index][p_index] = dp[s_index - 1][p_index - 1]
    #         if p[p_index] == '*':
    #             dp[s_index][p_index] = dp[s_index][p_index - 2] or dp[s_index][p_index - 1] or dp[s_index - 1][p_index]
    #         s_index += 1
    #         p_index += 1
    #     return dp[-1][-1]
    # endregion


# leetcode submit region end(Prohibit modification and deletion)

s = 'abc'
p = '.*c'
print(Solution().isMatch(s, p))
