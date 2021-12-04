# 你的任务是计算 ab 对 1337 取模，a 是一个正整数，b 是一个非常大的正整数且会以数组形式给出。
# 示例 1：

# 输入：a = 2, b = [3]
# 输出：8
# 示例 2：

# 输入：a = 2, b = [1,0]
# 输出：1024
# 示例 3：

# 输入：a = 1, b = [4,3,3,8,5,2]
# 输出：1
# 示例 4：

# 输入：a = 2147483647, b = [2,0,0]
# 输出：1198

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/super-pow
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# form https://leetcode-cn.com/problems/super-pow/solution/wu-xu-fu-zhu-han-shu-jian-ji-de-di-gui-xie-fa-by-m/
class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # a ** 213 =( a ** 210 ) * (a ** 3)
        base = 1337
        if not b:
            return 1
        # 获取最后一位数字
        last_value = b.pop()
        # (a ** 3)
        last_part = (a ** last_value) % base
        # ( a ** 210 )
        other_part = (self.superPow(a, b) ** 10) % base
        return (last_part * other_part) % base


solution = Solution()
a = 2147483647
b = [2, 1, 3]
result = solution.superPow(a, b)
print(f"a:{a},b:{b},result:{result}")
