# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。 
# 
#  示例 1: 
# 
#  输入: 123
# 输出: 321
#  
# 
#  示例 2: 
# 
#  输入: -123
# 输出: -321
#  
# 
#  示例 3: 
# 
#  输入: 120
# 输出: 21
#  
# 
#  注意: 
# 
#  假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231, 231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。 
#  Related Topics 数学 
#  👍 2221 👎 0

# Begin Time: 2020-09-30 17:45:56
# 执行耗时:48 ms,击败了45.37% 的Python3用户
# 内存消耗:13.4 MB,击败了31.61% 的Python3用户
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverse(self, x: int) -> int:
        MAX = int(2 ** 31 - 1)  # 2147483647
        MAX_DIV_10 = MAX // 10
        MIN = int(-2 ** 31)  # -2147483648
        flag = 0 if x < 0 else 1  # 符号
        if x == MIN:
            return 0
        x = x if flag else -x
        output = 0
        while x != 0:
            c = x % 10
            x = x // 10
            if output > MAX_DIV_10:
                return 0
            output = output * 10 + c
        output = output if flag else -output
        return output


# leetcode submit region end(Prohibit modification and deletion)


print(Solution().reverse(1563847412))
