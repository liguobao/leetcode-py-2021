class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        one_house = costs[0]
        red_count = len(one_house)
        pre_cost = costs[0]
        for i in range(0,n):
            cur_cost = []
            for j in range(red_count):
                cur_i_j_cost = []
                for i_i in range(0,n):
                    if i_i != i:
                       cur_i_j_cost.append(costs[i_i][j])
                cur_i_j_cost.append(costs[i][j])
                cur_cost.append(min(cur_i_j_cost))
            pre_cost = cur_cost
        print(pre_cost)
        return min(pre_cost)


solution = Solution()

input = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
result = solution.minCostII(input)
print(f"input:{input},result:{result}")


input = [[1, 5, 3], [2, 9, 4]]
result = solution.minCostII(input)
print(f"input:{input},result:{result}")
