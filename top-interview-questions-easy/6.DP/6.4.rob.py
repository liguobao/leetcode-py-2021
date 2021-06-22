# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，
# 影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
# 给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

class Solution(object):
    # dp[i] = Math.max(dp[i - 2] + nums[i], dp[i - 1]);
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        dp0 = 0  # 第1家没偷
        dp1 = nums[0]  # 第1家偷了
        for index in range(1, nums_len):
            # 先看一下前面前面偷和没偷谁更划算，然后存储到current_dp0，最后再赋值给dp0
            current_dp0 = max(dp0, dp1)
            # 把当前房子偷了，就是dp1
            dp1 = dp0 + nums[index]
            # 把上一个没偷的结果赋值回给dp0
            dp0 = current_dp0
        return max(dp0, dp1)


solution = Solution()
nums = [1, 2, 3, 1]
result = solution.rob(nums)
print(result)

nums = [2, 7, 9, 3, 1]
result = solution.rob(nums)
print(result)
