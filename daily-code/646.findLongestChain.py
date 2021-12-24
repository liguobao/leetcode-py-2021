class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        n = len(pairs)
        pairs.sort()
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)
pairs = [[1,2], [2,3], [3,4]]
result = Solution().findLongestChain(pairs)
print(f"pairs:{pairs},result:{result}")