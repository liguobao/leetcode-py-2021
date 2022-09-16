class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        # 右侧的匹配值
        paris = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in paris:
                # 没有可以匹配的值了
                if not stack:
                    return False
                # 当前是右边，对应栈的值不等于左侧
                if stack[-1] != paris[c]:
                    return False
                # 没问题的情况下，把栈弹出一个元素
                stack.pop()
            else:
                stack.append(c)
        return not stack

result = Solution().isValid("{()}")
print(result)
