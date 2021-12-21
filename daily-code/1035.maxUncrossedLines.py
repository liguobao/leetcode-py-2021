class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # dp[i][j] 表示 num1[0:i] + num2[0:j]
        # num1[i-1] == num2[j-1]
        n, m = len(nums1), len(nums2)
        dp = [[0] * (m+1) for _ in range(0, n+1)]
        for i in range(1, n + 1):
            for j in range(1, m+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


nums1 = [1, 4, 2]
nums2 = [1, 2, 4]
solution = Solution()
result = solution.maxUncrossedLines(nums1, nums2)
print(f"nums1:{nums1},nums2:{nums2},result:{result},")
