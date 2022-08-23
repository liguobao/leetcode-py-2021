

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        results = set()
        s_len = len(s)
        sub_dict = {}
        for index in range(s_len - 10+1):
            sub_str = s[index:index + 10]
            if sub_str not in sub_dict:
                 sub_dict[sub_str] = 0
            sub_dict[sub_str] = sub_dict[sub_str] + 1
            if sub_dict[sub_str] == 2:
                results.add(sub_str)
        return [x for x in results]


s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = Solution().findRepeatedDnaSequences(s)
print(f"{s},result:{result}")
