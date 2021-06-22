class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        # 初始值
        start_text = "1"
        for n_val in range(1, n):
            current_text = ""
            n_text = ""
            # 上一个值在这里
            for i in start_text:
                # 当前没有值，或者当前i的值等于上一个值的末尾，这种情况直接添加i到当前值后面
                if not current_text or i == current_text[-1]:
                    current_text = current_text + i
                else:
                    # 否则在全局值里面添加n个current_text的current_text[0]
                    n_text = n_text + f"{len(current_text)}{current_text[0]}"
                    current_text = i
            if current_text:
                n_text += "%s%s" % (len(current_text), current_text[0])
            start_text = n_text
        return start_text


solution_test = Solution()
result = solution_test.countAndSay(1)
print(result)

result = solution_test.countAndSay(2)
print(result)

result = solution_test.countAndSay(3)
print(result)


result = solution_test.countAndSay(4)
print(result)
