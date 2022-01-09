class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(n) = f(n-1) + f(n-2)
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

    def fib2(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f(n) = f(n-1) + f(n-2)
        if n == 0:
            return 0
        if n == 1:
            return 1
        f0 = 0
        f1 = 0
        result = 1
        for i in range(2, n+1):
            f1 = result
            f1 = f0
            result = f1 + f0
        return result


solution = Solution()
input_num = 10
result = solution.fib(input_num)
print(f"input_num:{input_num},result:{result}")
