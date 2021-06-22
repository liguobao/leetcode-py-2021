class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_day = len(prices)
        if total_day == 0:
            return 0
        last_day_price = prices[0]
        total_profit = 0
        for price_index in range(0, total_day):
            today_price = prices[price_index]
            if today_price > last_day_price:
                total_profit = total_profit + today_price - last_day_price
            last_day_price = today_price
        return total_profit


nums = [7, 1, 5, 3, 6, 4]
solution_test = Solution()
print(nums)
result = solution_test.maxProfit(nums)
print(result)
