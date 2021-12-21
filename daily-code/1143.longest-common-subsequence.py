class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j] = text1[0:i] 和 text2[0:j]的最长子序列长度
        # text1[i-1] == text2[j-1], 则可见 dp[i][j] = dp[i-1][j-1] + 1
        # text1[i-1] != text2[j-1], 
        # 则两种情况： text1[0:i-1] + text2[0:j]  -> dp[i-1][j]
        # 或者 text1[0:i] + text2[0:j-1] -> dp[i][j-1]
        n, m = len(text1), len(text2)
        dp = [[0] * (m+1) for _ in range(0, n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[n][m]


text1 = "abdn"
text2 = "ab"
solution = Solution()
result = solution.longestCommonSubsequence(text1, text2)
print(f"text1:{text1},text2:{text2},result:{result},")
