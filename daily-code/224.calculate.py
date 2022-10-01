class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_stack = []
        result = 0
        prev_num = ""
        for x in s:
            if x in [" ", "-", "+", "("]:
                if len(prev_num):
                    num_stack.append(int(prev_num))
                    prev_num = ""
                if x == " ":
                    continue
                num_stack.append(x)
                continue
            elif x == ")":
                if len(prev_num):
                    num_stack.append(int(prev_num))
                    prev_num = ""
                head_num = num_stack.pop()
                sub_nums = []
                while head_num != "(":
                    sub_nums.append(head_num)
                    head_num = num_stack.pop()
                prev_item = ""
                sub_nums.reverse()
                sub_result = 0
                for sub_x in sub_nums:
                    if sub_x != "-" and sub_x != "+":
                        if prev_item == "-":
                            sub_result = sub_result - int(sub_x)
                        else:
                            sub_result = sub_result + int(sub_x)
                    else:
                        prev_item = sub_x
                num_stack.append(sub_result)
            else:
                prev_num = prev_num + x
        sub_nums = []
        if len(prev_num):
            num_stack.append(int(prev_num))
            prev_num = ""
        while num_stack:
            head_num = num_stack.pop()
            sub_nums.append(head_num)
        prev_item = ""
        sub_nums.reverse()
        last_result = 0
        if len(sub_nums):
            for sub_x in sub_nums:
                if sub_x != "-" and sub_x != "+":
                    if prev_item == "-":
                        last_result = last_result - int(sub_x)
                    else:
                        last_result = last_result + int(sub_x)
                else:
                    prev_item = sub_x
        if prev_item == "-":
            result = last_result + (-result)
        else:
            result = last_result + result
        return result

s = "1112"
result = Solution().calculate(s)
print(f"s:{s},result:{result}")

s = "1-(     -2)"
result = Solution().calculate(s)
print(f"s:{s},result:{result}")

s = "(1-(3-4))"
result = Solution().calculate(s)
print(f"s:{s},result:{result}")
