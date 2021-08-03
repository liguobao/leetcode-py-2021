class Solution():
    def __init__(self) -> None:
        pass

    def init_dp(self, pat):
        self.pat_len = len(pat)
        self.pat = pat
        self.dp = [[0 for i in range(255)] for j in range(self.pat_len)]
        self.dp[0][ord(pat[0])] = 1
        X = 0
        for j in range(self.pat_len):
            for c in range(255):
                pat_c = pat[j]
                if ord(pat_c) == c:
                    self.dp[j][c] = j + 1
                else:
                    self.dp[j][c] = self.dp[X][c]
            pat_c = pat[j]
            X = self.dp[X][ord(pat_c)]
        print(self.dp)

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
solution.init_dp("ababc")
result = solution.search_by_pat("abc", "abaababcc")
print(result)
result = solution.search_by_pat("cba", "aaaababcc")
print(result)
result = solution.search_by_pat("a", "aaaababcc")
print(result)
