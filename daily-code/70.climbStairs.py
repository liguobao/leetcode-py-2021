# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

# 注意：给定 n 是一个正整数。

# 示例 1：

# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：

# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/climbing-stairs
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 1
        f1 =0
        f2 =0
        # 达到第n阶台阶的总可能性 f(n) = f(n-1) + f(n-2)
        for i in range(1, n+1):
            f2 =f1
            f1 = result
            result = f1 + f2
        return result


solution = Solution()
input_num = 2
result = solution.climbStairs(input_num)
print(f"input_num:{input_num},result:{result}")