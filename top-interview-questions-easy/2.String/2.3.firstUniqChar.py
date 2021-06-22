# https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_dict = {}
        s_index_list = []
        for s_index in range(0, len(s)):
            item = s[s_index]
            if item in s_dict:
                s_dict[item]["count"] = s_dict[item]["count"] + 1
            else:
                s_dict[item] = {"count": 1, "s_index": s_index}
                s_index_list.append(item)
        for item in s_index_list:
            if s_dict[item]["count"] == 1:
                return s_dict[item]["s_index"]
        return -1


s_value = "leetcode"
print(s_value)
solution_test = Solution()
result = solution_test.firstUniqChar(s_value)
print(result)
