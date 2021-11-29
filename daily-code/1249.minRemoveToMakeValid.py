class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # 右括号
        right = []
        # 左括号
        left = []
        for i, c in enumerate(s):
            # 当前值为左括号，添加到左栈
            if c == "(":
                left.append(i)
            elif c ==")": 
                # 当前值为右括号，
                # 如果有左括号栈有数据，说明是匹配的，这时直接左括号出栈一个
                # 如果当前左括号是空白的，说明当前有括号无效，扔掉
                if left:
                    left.pop()
                else:
                    right.append(i)
        # 所有需要移除的数据
        remove_index_list = set(right) | set(left)
        return "".join([ c for i,c in enumerate(s) if i not in remove_index_list])

solution = Solution()
input_text = "lee(t(c)o)de)"
result = solution.minRemoveToMakeValid(input_text)
print(f"{input_text} --> {result}")