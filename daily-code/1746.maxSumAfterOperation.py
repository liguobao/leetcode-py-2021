# 你有一个整数数组 nums。你只能将一个元素 nums[i] 替换为 nums[i] * nums[i]。

# 返回替换后的最大子数组和。

#  

# 示例 1：

# 输入：nums = [2,-1,-4,-3]
# 输出：17
# 解释：你可以把-4替换为16(-4*(-4))，使nums = [2,-1,16,-3]. 现在，最大子数组和为 2 + -1 + 16 = 17.
# 示例 2：

# 输入：nums = [1,-1,1,1,-1,-1,1]
# 输出：4
# 解释：你可以把第一个-1替换为1，使 nums = [1,1,1,1,-1,-1,1]. 现在，最大子数组和为 1 + 1 + 1 + 1 = 4.

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def maxSumAfterOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = len(nums)
        dp = [[0, 0] for x in range(0, nums_count)]
        # dp[i][0] 没有出现过相乘 dp[i][0] = max(dp[i-1][0] + nums[i],nums[i])
        # dp_i_max = max(dp[i-1][1]+nums[i], dp[i-1][0]+nums[i] * nums[i])
        # dp[i][1] 当前i自乘 dp[i][1] = max(dp_i_max, nums[i] * nums[i])
        dp[0][0] = nums[0]
        dp[0][1] = nums[0] * nums[0]
        result = dp[0][1] 
        for i in range(0, nums_count):
            # 前一个已经相乘 + 当前值 | 前一个未相乘 + 当前值相乘 | 当前值直接相乘
            dp[i][1] = max(
                dp[i-1][1] + nums[i], 
                dp[i-1][0] + nums[i] * nums[i], 
                nums[i] * nums[i])
            # 前一个 + 当前值 | 当前值
            dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
            result = max(result, dp[i][1])
        return result


solution = Solution()
nums = [2, -1, -4, -3]
result = solution.maxSumAfterOperation(nums)
print(result)
