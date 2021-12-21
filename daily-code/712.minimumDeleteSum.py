class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m, n = len(s1), len(s2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        def get_total_ascii(s):
            return sum([ord(c) for c in s])
        # dp[i][j]
        #  题意是寻找一个共同子序列，将字符串s1和s2删除为该子序列时所删除的ASCII综合最小。
        # 等价于求一个字符串s1和s2的ASCII码总和最大的共同子序列。
        # 因为s1和s2的总和固定，当共同子序列的总和最大时，删除成为该子序列的代价必然最小。

        # 作者：falcon-2
        # 链接：https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/solution/asciima-zui-da-de-zi-xu-lie-zui-chang-gong-tong-zi/
        # 来源：力扣（LeetCode）
        # 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return get_total_ascii(s1) + get_total_ascii(s2) - 2*dp[-1][-1]


s1 = "sea"
s2 = "eat"
result = Solution().minimumDeleteSum(s1, s2)
print(f"s1:{s1},s2:{s2},result:{result}")
