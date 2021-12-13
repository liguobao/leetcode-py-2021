# 给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。

# 示例 1：

# 输入：[1,0,1,1,0]
# 输出：4
# 解释：翻转第一个 0 可以得到最长的连续 1。
#      当翻转以后，最大连续 1 的个数为 4。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = len(nums)
        dp = [[0, 0] for x in range(nums_count + 1)]
        result = 0
        for i in range(1, nums_count + 1):
            item_value = nums[i-1]
            # item_value = 1, dp[i][0] | dp[i][1] 都等于 前一个结果 + 1
            # item_value =0, dp[i][0] 不能翻转，所以结果为0
            # item_value =0, dp[i][1] 可以翻转，当前翻转，所以前面的没有翻转过，dp[i][1] = dp[i-1][0] + 1
            if item_value == 1:
                dp[i][0] = dp[i-1][0] + 1
                dp[i][0] = dp[i-1][0] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0] + 1
            result = max(result, dp[i][0],  dp[i][1])
        return result
            


solutuon = Solution()
nums = [1, 0, 1, 1, 0]
results = solutuon.findMaxConsecutiveOnes(nums=nums)
print(f"nums:{nums},result:{results}")
