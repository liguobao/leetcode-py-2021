class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        if ch not in word:
            return word
        ch_index = word.index(ch)
        sub_text = word[0:ch_index+1]
        rev_text = sub_text[::-1]
        # rev_text = "".join(reversed(sub_text))
        remove_text = word.replace(sub_text, rev_text)
        return remove_text


word = "abcdefd"
ch = "d"
result = Solution().reversePrefix(word, ch)
print(f"input_text:{word},{ch},result:{result}")
