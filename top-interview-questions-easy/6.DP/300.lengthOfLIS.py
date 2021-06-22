# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3, 6, 2, 7] 是数组[0, 3, 1, 6, 2, 2, 7] 的子序列。

# 来源：力扣（LeetCode）
# 链接：https: // leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# f(n) = max(f(n-1), f(n-2))

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 2:
            return 1
        dp = []
        for i in range(0, nums_len):
            # 1 表示当前这个位置 dp[i]的原始值
            # 下面会检查原始值是否需要被替换
            dp.append(1)
            # 遍历前i个dp的值
            for j in range(i):
                # 如果当前的nums[i]比nums[j]大，
                # 则说明要dp[i]要不是原始的dp[i],
                # 要不是前dp[j] 加上当前这个数值，就是 dp[j] + 1
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


solution = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = solution.lengthOfLIS(nums)
print(result)
