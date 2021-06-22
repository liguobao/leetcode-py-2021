class Solution(object):
    # 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        current = nums[0]
        max_sub = current
        for index in range(1, len(nums)):
            # 前置的值如果小于0，舍弃；比0大则说明有价值
            # 继续累加到当前结果
            current = max(current, 0) + nums[index]
            # 最大值就看之前的最大值和当前子序列总和比较，取最大的
            max_sub = max(current, max_sub)
        return max_sub


solution = Solution()
prices = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = solution.maxSubArray(prices)
print(result)

prices = [7, 6, 4, 3, 1]
result = solution.maxSubArray(prices)
print(result)
