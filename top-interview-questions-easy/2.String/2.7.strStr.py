# https://leetcode-cn.com/problems/implement-strstr/
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needle_len = len(needle)
        if needle_len == 0:
            return 0
        first_needle_item = needle[0]
        for h_index, h_val in enumerate(haystack):
            if h_val == first_needle_item:
                h_needle = haystack[h_index:h_index+needle_len]
                if h_needle == needle:
                    return h_index
        return -1


haystack = "hello"
needle = "ll"
print(f"haystack:{haystack},needle:{needle}")
solution_test = Solution()
result = solution_test.strStr(haystack, needle)
print(result)
