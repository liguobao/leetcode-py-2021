# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        s_dict = {}
        for item in s:
            if item not in s_dict:
                s_dict[item] = 0
            s_dict[item] = s_dict[item] + 1
        t_dict = {}
        for item in t:
            if item not in t_dict:
                t_dict[item] = 0
            t_dict[item] = t_dict[item] + 1
        for key in s_dict.keys():
            s_item = s_dict[key]
            if key not in t_dict:
                return False
            t_item = t_dict[key]
            if t_item != s_item:
                return False
        return True


s_value = "aacc"
t_value = "ccac"
print(s_value)
solution_test = Solution()
result = solution_test.isAnagram(s_value, t_value)
print(result)
