class Solution:
    def minCost(self, costs):
        n = len(costs)
        pre_0 = costs[0][0]
        pre_1 = costs[0][1]
        pre_2 = costs[0][2]
        for i in range(1, n):
            # 当前的选择颜色0，则上一个一定是 1 或者 2
            cur_0 = min(costs[i][0] + pre_1, costs[i][0] + pre_2)
            cur_1 = min(costs[i][1] + pre_0, costs[i][1] + pre_2)
            cur_2 = min(costs[i][2] + pre_0, costs[i][2] + pre_1)
            
            pre_0 = cur_0
            pre_1 = cur_1
            pre_2 = cur_2

        return min(pre_2, pre_1, pre_0)