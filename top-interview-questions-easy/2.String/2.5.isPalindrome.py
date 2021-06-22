# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text_array = []
        min_num = ord("0")
        max_num = ord("9")
        A_num = ord("A")
        Z_num = ord("Z")
        a_num = ord("a")
        z_num = ord("z")
        text_array = list(
            [x.lower() for x in s if A_num <= ord(x) <= Z_num or a_num <= ord(x) <= z_num or min_num <= ord(x) <= max_num])
        text_len = len(text_array)
        if text_len <= 0:
            return True
        start_index = 0
        end_index = text_len - 1
        while start_index != end_index:
            start_value = text_array[start_index]
            end_value = text_array[end_index]
            if start_value != end_value:
                return False
            start_index += 1
            end_index -= 1
            if end_index < 0:
                break
        return True


s_value = "ab_a"
print(s_value)
solution_test = Solution()
result = solution_test.isPalindrome(s_value)
print(result)
