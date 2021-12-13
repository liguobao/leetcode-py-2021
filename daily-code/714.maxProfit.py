class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # f[i][0] 表示第i天没有股票的收益
        # f[i][1] 表示第i天有股票的收益
        prices_count = len(prices)
        dp = [[0, -prices[0]]] + [[0, 0] for x in range(prices_count-1)]
        for i in range(1, prices_count):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i-1][0] - prices[i], dp[i-1][1])
        return dp[prices_count-1][0]


solution = Solution()
prices = [1, 3, 2, 8, 4, 9]
fee = 2
result = solution.maxProfit(prices=prices, fee=fee)
print(f"prices:{prices},fee:{fee},result:{result}")













        # f[i][0] 表示第i天没有股票的收益，则要不 i-1天有股票，i天卖出，花掉 fee手续费；要不 i-1天没有股票，则f[i-1][0]
        # f[i][0] = max(f[i-1][1] + prices[i] - fee, f[i-1][0])
        # f[i][1] 表示第i天有股票的收益，则要不i-1没有股票，i天买入；要不第i-1天有股票，i天不动
        # f[i][1] = max(f[i-1][0] - prices[i], f[i-1][1])