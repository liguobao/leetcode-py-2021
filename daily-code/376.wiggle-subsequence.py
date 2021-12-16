
# 解题思路
# 状态定义
# dp[i][0]: 第i元素结尾，且最后上升的最长子序列长度 ↑
# dp[i][1]: 第i元素结尾，且最后下降的最长子序列长度 ↓
# 状态转移：
# if nums[i] < nums[i-1] : 新的尾结点下降
# dp[i][1] = dp[i-1][0] + 1
# dp[i][0] = dp[i-1][0]
# if nums[i] > nums[i-1] : 新的尾结点上升
# dp[i][0] = dp[i-1][1] + 1
# dp[i][1] = dp[i-1][1]
# if nums[i] = nums[i-1] : 新的尾结点不变
# dp[i][0] = dp[i-1][0]
# dp[i][1] = dp[i-1][1]
# 边界情况：dp[0] = [1,1]

# 作者：caiji-ud
# 链接：https://leetcode-cn.com/problems/wiggle-subsequence/solution/python3-dong-tai-gui-hua-by-caiji-ud-o3hz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


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
                dp[i][0] = dp[i-1][0] # 上升数组，继续保持上升值
                dp[i][1] = dp[i-1][0] + 1 # 下降数组，此时等于前一个上升数组 +1
            elif nums[i] > nums[i-1]: # 尾结点上升
                dp[i][0] = dp[i-1][1] + 1 # 上升数组，等于前一个下降数组值 +！
                dp[i][1] = dp[i-1][1] # 下降数组，保持不变
            else: # 相等的情况下，继续保持不变
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        return max(dp[nums_count-1][0], dp[nums_count-1][1])


solutuon = Solution()
nums = [1, 7, 4, 9, 2, 5]
result = solutuon.wiggleMaxLength(nums)
print(f"nums:{nums},result:{result}")
