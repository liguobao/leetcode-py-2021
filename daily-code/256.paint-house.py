class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        # 第一个房子的三种可能性需要花费的费用
        pre_0 = costs[0][0]
        pre_1 = costs[0][1]
        pre_2 = costs[0][2]
        for i in range(1, n):
            # 第i个房子：min( 0 + pre_1, 0 + pre_2)
            # 当前的选择颜色0，则上一个一定是 1 或者 2
            cur_0 = min(costs[i][0] + pre_1, costs[i][0] + pre_2)
            cur_1 = min(costs[i][1] + pre_0, costs[i][1] + pre_2)
            cur_2 = min(costs[i][2] + pre_0, costs[i][2] + pre_1)
            pre_0 = cur_0
            pre_1 = cur_1
            pre_2 = cur_2
        return min(pre_0, pre_1, pre_2)


solutuon = Solution()
costs = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
result = solutuon.minCost(costs)
print(f"costs:{costs},result:{result}")

costs = [[7, 6, 2]]
result = solutuon.minCost(costs)
print(f"costs:{costs},result:{result}")
