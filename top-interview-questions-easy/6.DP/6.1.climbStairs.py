class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 如果小于等于1阶梯，只有一个答案
        if n <= 1:
            return 1
        # 初始化1、2阶梯的走法
        results = [1, 2]
        # 从第三阶梯开始，后面的每个阶梯其实都等于前面阶梯的累加
        # f(n) = f(n-1) + f(n-2)
        for index in range(2, n+1):
            results.append(results[index - 1] + results[index - 2])
        return results[n-1]


solution = Solution()

result = solution.climbStairs(2)
print(result)

result = solution.climbStairs(3)
print(result)
