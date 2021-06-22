class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        prices_len = len(prices)
        if prices_len <= 1:
            return 0
        # 起始值，第一天的价格
        pre_day_price = prices[0]
        for index in range(1, prices_len):
            current_price = prices[index]
            # 当前的最大有益
            current_profit = current_price - pre_day_price
            # 如果当前最大收益大于全局最大收益，覆盖全局
            if current_profit > max_profit:
                max_profit = current_profit
            # 如果当前价格小于当前的起始价格，把起始价格覆盖
            if current_price < pre_day_price:
                pre_day_price = current_price
        return max_profit


solution = Solution()
prices = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(prices)
print(result)

prices = [7, 6, 4, 3, 1]
result = solution.maxProfit(prices)
print(result)
