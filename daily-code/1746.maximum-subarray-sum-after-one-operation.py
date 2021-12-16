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
        for i in range(1, nums_count):
            # 前一个自乘 + 当前值 | 前一个未自乘 + 当前值自乘 | 当前自乘
            # 取最大值
            dp_i_1_max = max(dp[i-1][1]+nums[i], dp[i-1]
                             [0] + nums[i] * nums[i])
            dp[i][1] = max(dp_i_1_max, nums[i]*nums[i])
            # 没有自乘 + 当前值 | 当前值
            dp[i][0] = max(dp[i-1][0] + nums[i], nums[i])
            result = max(result, dp[i][1])
        return result


solution = Solution()
nums = [2, -1, -4, -3]
result = solution.maxSumAfterOperation(nums)
print(result)
