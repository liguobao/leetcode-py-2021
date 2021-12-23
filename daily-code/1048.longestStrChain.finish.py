class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def word_contians(word1, word2):
            m, n = len(word1), len(word2)
            w1_array = list(word1)
            w2_array = list(word2)
            if m+1 != n:
                return False
            un_word = list(set(w1_array)^set(w2_array))
            if len(un_word) >0:
                one_c = un_word[0]
                for i in range(m+1):
                    w_array = w1_array.copy()
                    w_array.insert(i, one_c)
                    if "".join(w_array) == word2:
                        return True
            else:
                for one_c in w2_array:
                    for i in range(m+1):
                        w_array = w1_array.copy()
                        w_array.insert(i, one_c)
                        if "".join(w_array) == word2:
                            return True         
            return False

        words.sort(key=lambda x: len(x))
        words_count = len(words)
        dp = [1] * words_count
        result = 0
        for i in range(words_count):
            for j in range(i):
                if word_contians(word1=words[j], word2=words[i]):
                    dp[i] = max(dp[i], dp[j]+1)
            result = max(result, dp[i])
        return result