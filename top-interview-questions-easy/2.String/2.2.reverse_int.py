class Solution(object):
    def reverse(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        first_num = s > 0
        int_value = s if first_num else - s
        r = 0
        while int_value != 0:
            r = r * 10
            end_num = int_value % 10
            int_value = int(int_value / 10)
            r = r + end_num
        r = r if first_num else -r
        if r < - 2 ** 31 or r > 2 ** 31:
            return 0
        return r


int_value = 1563847412
print(int_value)
solution_test = Solution()
result = solution_test.reverse(int_value)
print(result)
