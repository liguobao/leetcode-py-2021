class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        f1 = 0
        f2 = 0
        sum = 1
        for i in range(2, n + 1):
            f2 = f1
            f1 = sum
            sum = f1 + f2
        return sum


solution = Solution()
input_num = 10
result = solution.fib(input_num)
print(f"input_num:{input_num},result:{result}")
