# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。 
# 
#  示例 1： 
# 
#  输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
#  
# 
#  示例 2： 
# 
#  输入: "cbbd"
# 输出: "bb"
#  
#  Related Topics 字符串 动态规划 
#  👍 2743 👎 0

# Begin Time: 2020-09-30 11:19:40
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    # 执行耗时:72 ms,击败了97.95% 的Python3用户
    # 内存消耗:13.3 MB,击败了85.61% 的Python3用户
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        length = len(s)
        if length == 1 or s == s[::-1]:
            return s
        max_len, start = 1, 0
        for i in range(1, length):
            even = s[i - max_len:i + 1]
            odd = s[i - max_len - 1:i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2  # max_len = i-start+1
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1  # max_len = i-start+1
                continue
        return s[start:start + max_len]

    # 动态规划
    # 执行耗时:4472 ms,击败了43.58% 的Python3用户
    # 内存消耗:21.7 MB,击败了12.67% 的Python3用户
    # def longestPalindrome(self, s: str) -> str:
    #     size = len(s)
    #     if size < 2:
    #         return s
    #
    #     dp = [[False for _ in range(size)] for _ in range(size)]
    #
    #     max_len = 1
    #     start = 0
    #
    #     for j in range(1, size):
    #         for i in range(0, j):
    #
    #             dp[i][j] = (s[i] == s[j]) and (j - i < 3 or dp[i + 1][j - 1])
    #
    #             if dp[i][j]:
    #                 cur_len = j - i + 1
    #                 if cur_len > max_len:
    #                     max_len = cur_len
    #                     start = i
    #     return s[start:start + max_len]


# leetcode submit region end(Prohibit modification and deletion)

inputs = "abccbbccbd"
print(Solution().longestPalindrome(inputs))
