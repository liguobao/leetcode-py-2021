class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        s_count = len(s)
        if s_count == 0:
            return s
        item_num = int(s_count / 2)
        for item_index in range(0, item_num):
            item_value = s[item_index]
            s[item_index] = s[s_count-item_index-1]
            s[s_count-item_index-1] = item_value
        return s


s_text = ["h", "e", "l", "l", "o"]
print(s_text)
solution_test = Solution()
result = solution_test.reverseString(s_text)
print(result)
