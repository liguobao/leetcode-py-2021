class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dp[i] = max(dp[j]) + 1 j < i && nums[j] < nums[i]
        if not nums or len(nums) == 0:
            return 0
        nums_len = len(nums)
        dp = []
        for i in range(0, nums_len):
            dp.append(1)
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = Solution().lengthOfLIS(nums)
print(f"nums:{nums},result:{result}")

nums = [0, 1, 0, 3, 2, 3]
result = Solution().lengthOfLIS(nums)
print(f"nums:{nums},result:{result}")
