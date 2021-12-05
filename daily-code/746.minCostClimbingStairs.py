# 746. 使用最小花费爬楼梯
# 数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i]（下标从 0 开始）。

# 每当你爬上一个阶梯你都要花费对应的体力值，一旦支付了相应的体力值，你就可以选择向上爬一个阶梯或者爬两个阶梯。

# 请你找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。


# 示例 1：

# 输入：cost = [10, 15, 20]
# 输出：15
# 解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
#  示例 2：

# 输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# 输出：6
# 解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。

class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # f(n) = min(f(n-1) + cost[n-1], f(n-2) + cost[n-2])
        # 到达顶点，要不前面一阶梯一步上去，要不前面两阶梯两步上去
        # 二选一，取最小的一个
        f1 = 0
        f2 = 0
        cost_sum = 0
        n = len(cost)
        for i in range(2, n+1):
            # 取最小的一个
            cost_sum = min(f1 + cost[i-1], f2 + cost[i-2])
            f2 = f1
            f1 = cost_sum
        return cost_sum


solution = Solution()
input = [10, 15, 20]
result = solution.minCostClimbingStairs(input)
print(f"input:{input},result:{result}")


input = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result = solution.minCostClimbingStairs(input)
print(f"input:{input},result:{result}")
