# 给你数字 k ，请你返回和为 k 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。
# 斐波那契数字定义为：
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 ， 其中 n > 2 。
# 数据保证对于给定的 k ，一定能找到可行解。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def findMinFibonacciNumbers(self, k):
        """
        :type k: int
        :rtype: int
        """
        nums = self.build_fibonacci_array()
        print(nums)

    def build_fibonacci_array(self):
        nums = [1, 2]
        for x in range(2, 50):
            nums.append(nums[x-1]+nums[x-2])
        return nums


k = 7
result = Solution().findMinFibonacciNumbers(k)
print(f"k:{k},result:{result}")
