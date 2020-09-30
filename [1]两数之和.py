# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9244 👎 0

# Begin Time: 2020-09-29 17:03:26
# Consume Time: 12:25
# 解答成功:
# 执行耗时:44 ms,击败了94.36% 的Python3用户
# 内存消耗:14.8 MB,击败了20.22% 的Python3用户

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i


# leetcode submit region end(Prohibit modification and deletion)

nums = [2, 7, 11, 15]
target = 9

print(Solution().twoSum(nums, target))
