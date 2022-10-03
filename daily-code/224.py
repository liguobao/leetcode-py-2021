class Solution(object):
    def calculate(self, s):
        result = 0
        # 存储了操作位的栈信息，当前作用域下的操作位，遇到（ 压栈，遇到 ） 出栈
        ops_stack = [1]
        # 遇到 + ，延续 ops_stack 中的操作符
        # 遇到 - ，取反 ops_stack 中的操作符
        sign = 1
        sCount = len(s)
        i = 0
        while i < sCount:
            # 不需要处理
            if s[i] == " ":
                i = i + 1
                continue
            # 遇到 +， 当前作用域操作符和ops_stack最后一个元素一致
            if s[i] == "+":
                sign = ops_stack[-1]
                i = i + 1
                continue
            # 遇到 - ，当前作用域操作符需要取反
            if s[i] == "-":
                sign = -ops_stack[-1]
                i = i + 1
                continue
            # 遇到 ( 意味着进入新的作用域，把上一个操作符压入栈（当前操作符可以作用域延续）
            if s[i] == "(":
                ops_stack.append(sign)
                i = i + 1
                continue
            # 遇到 ） 意味着当前作用域结束，把栈中最后一个操作符干掉
            if s[i] == ")":
                ops_stack.pop()
                i = i + 1
                continue
            # 上面都不是，开始计算当前数字是多少（字符串转数字）
            num = 0
            while i < sCount and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
                i = i + 1
            # 计算完了之后，使用当前符号位 * num，累加到结果即可
            result = result + num * sign
        return result


# s = "1112"
# result = Solution().calculate(s)
# print(f"s:{s},result:{result}")

s = "1-(-2)"
result = Solution().calculate(s)
print(f"s:{s},result:{result}")
