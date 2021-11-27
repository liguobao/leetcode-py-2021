from typing import Text


class Solution():
    def __init__(self) -> None:
        pass

    def init_dp(self, pat):
        self.pat_len = len(pat)
        self.pat = pat
        self.dp = [[0 for i in range(255)] for j in range(self.pat_len)]
        first_c = ord(pat[0])
        self.dp[0][first_c] = 1
        X = 0
        for j in range(1, self.pat_len):
            # j pat字符串第j个元素
            pat_c = pat[j]
            pat_c_val = ord(pat_c)
            for c in range(255):
                if pat_c_val == c:
                    self.dp[j][c] = j + 1
                else:
                    self.dp[j][c] = self.dp[X][c]
            X = self.dp[X][pat_c_val]
    
    def search(self, txt):
        M = self.pat_len
        N = len(txt)
        # pat 的初始态为 0
        j = 0
        for i in range(N):
            # 当前是状态 j，遇到字符 txt[i]，
            # pat 应该转移到哪个状态？
            txt_c = txt[i]
            j = self.dp[j][ord(txt_c)]
            # 如果达到终止态，返回匹配开头的索引
            if (j == M):
                return i - M + 1
        #没到达终止态，匹配失败
        return -1


    def search_by_pat(self, pat, text):
        pat_len = len(pat)
        text_len = len(text)
        for i in range(0, text_len - pat_len):
            for j in range(0, pat_len):
                if pat[j] != text[i+j]:
                    j = 0
                    break
            if j == pat_len-1:
                return i
        return -1


solution = Solution()
solution.init_dp("ABABC")
result = solution.search("AAA")
print(result)
result = solution.search("AAABABCCCC")
print(result)
result = solution.search("CCCCAABABCCCC")
print(result)
result = solution.search_by_pat("abc", "abaababcc")
print(result)
result = solution.search_by_pat("cba", "aaaababcc")
print(result)
result = solution.search_by_pat("a", "aaaababcc")
print(result)
