class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i][0] 最后上升的最长子序列
        # dp[i][1] 最后下降的最长子序列
        nums_count = len(nums)
        if nums_count < 2:
            return 1
        dp = [[1, 1] for x in range(nums_count)]
        for i in range(1, nums_count):
            if nums[i] < nums[i-1]:  # 尾结点下降
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][0] + 1
            elif nums[i] > nums[i-1]:
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = dp[i-1][1]
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        return max(dp[nums_count-1][0], dp[nums_count-1][1])


solutuon = Solution()
nums = [1, 7, 4, 9, 2, 5]
result = solutuon.wiggleMaxLength(nums)
print(f"nums:{nums},result:{result}")
