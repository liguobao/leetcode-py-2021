# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。
# 例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


# dp[i]=max(dp[j])+1,其中0≤j<i且num[j]<num[i]
# 

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
                #  nums[i] >  nums[j]的时候，
                # 当前dp[i] 取 dp[i] 和 dp[j] +1 的最大值
                # 然后 j ++ ，继续去寻找有没有比dp[i] 更大的 dp[j]
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = Solution().lengthOfLIS(nums)
print(f"nums:{nums},result:{result}")

nums = [0, 1, 0, 3, 2, 3]
result = Solution().lengthOfLIS(nums)
print(f"nums:{nums},result:{result}")
