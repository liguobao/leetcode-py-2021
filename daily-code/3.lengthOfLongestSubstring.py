class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        lookup = set()
        left =0
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len = cur_len +1
            while s[i] in lookup:
                # 把左侧的元素移走
                lookup.remove(s[left])
                # 同时移动
                left = left +1
                cur_len = cur_len -1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len

result = Solution().lengthOfLongestSubstring("abcdaaa")
print(result)