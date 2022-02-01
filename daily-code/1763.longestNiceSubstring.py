class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0:
            return ""
        d_dict = {}
        for ord_val in range(ord("a"), ord("a") + 26):
            d_dict[chr(ord_val)] = chr(ord_val-(ord("a") - ord("A")))
        
        for ord_val in range(ord("A"), ord("A") + 26):
            d_dict[chr(ord_val)] = chr(ord_val+(ord("a") - ord("A")))

        def check_nice(sub_text):
            # 去重set
            w = set(sub_text)
            for c in w:
                if d_dict[c] not in w:
                    return False
            return True
        ans = ""
        long_count = 0
        s_count = len(s)
        for i in range(s_count-1):
            for j in range(i + long_count, s_count):
                new_text = s[i:j+1]
                if check_nice(new_text) and j-i > long_count:
                    long_count = j - i
                    ans = new_text
        return ans


input_text = "Bb"
result = Solution().longestNiceSubstring(input_text)
print(f"input_text:{input_text},result:{result}")

input_text = "YazaAay"
result = Solution().longestNiceSubstring(input_text)
print(f"input_text:{input_text},result:{result}")
