class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 状态转移：
        # i = 1: dp[i][0] = dp[i-1][0]+1 在前面的基础上 + 1
        # i = 1: dp[i][1] = dp[i-1][1]+1 在前面的基础上 + 1
        # i = 0: dp[i][0] = 0 不能使用翻转,所以遇到0就置0 
        # i = 0: dp[i][1] = dp[i-1][0]+1 基于未操作的序列转移 

        # 作者：caiji-ud
        # 链接：https://leetcode-cn.com/problems/max-consecutive-ones-ii/solution/python3-dong-tai-gui-hua-by-caiji-ud-awny/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        nums_count = len(nums)
        dp = [[0, 0] for _ in range(nums_count+1)]
        result = 0
        for i in range(1, nums_count + 1):
            item = nums[i-1]
            if item ==1:
                dp[i][0] = dp[i-1][0] +1
                dp[i][1] = dp[i-1][1] + 1
            else:
                dp[i][0] = 0
                dp[i][1] = dp[i-1][0] +1
            result = max(result, dp[i][0], dp[i][1])
        return result


solutuon = Solution()
nums = [1, 0, 1, 1, 0]
results = solutuon.findMaxConsecutiveOnes(nums=nums)
print(f"nums:{nums},result:{results}")
