# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4381 👎 0

# Begin Time: 2020-09-29 18:58:13
# 执行耗时:72 ms,击败了81.08% 的Python3用户
# 内存消耗:13.5 MB,击败了30.45% 的Python3用户

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        output = 0
        left = 0
        right = 1
        while right < length:
            if s[right] in s[left:right]:
                output = right - left if right - left > output else output
                left += 1
            else:
                right += 1
        output = right - left if right - left > output else output
        return output


# leetcode submit region end(Prohibit modification and deletion)

inputs = 'dvdf'
print(Solution().lengthOfLongestSubstring(inputs))
