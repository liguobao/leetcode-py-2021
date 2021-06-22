class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_array = []
        min_num = ord("0")
        max_num = ord("9")
        _num = ord("-")
        is_negative = False
        is_first_negative = False
        is_first_zero = False
        is_first_native = False
        s = s.strip()
        for item_index, item, in enumerate(s):
            item_val = ord(item)
            if item != "-" and item != "+" and item != "0" and item != " " and item_index == 0 and (item_val < min_num or item_val > max_num):
                return 0
            if item == "-" and item_index == 0 and is_negative is False:
                is_negative = True
            if is_first_native and is_negative:
                return 0
            if is_first_native and (item_val < min_num or item_val > max_num) and len(num_array) == 0:
                return 0
            if is_first_negative and (item_val < min_num or item_val > max_num) and len(num_array) == 0:
                return 0
            if item_index == 0 and item == "-":
                is_first_negative = True
            if item_index == 0 and item == "+":
                is_first_native = True
            if item_index == 0 and item == "0":
                is_first_zero = True
            if is_first_negative and item == "+" and len(num_array) == 0:
                return 0
            if is_first_zero and is_negative:
                return 0
            if item_val < min_num or item_val > max_num:
                if len(num_array) > 0:
                    break
                continue
            num_array.append(item)
        num_array_len = len(num_array)
        result_num = 0
        ten_x = 0
        while num_array_len > 0:
            result_num = result_num + 10 ** ten_x * \
                int(num_array[num_array_len-1])
            num_array_len = num_array_len-1
            ten_x = ten_x+1
        if is_negative:
            result_num = - result_num
        if 0 < result_num < 2 ** 31:
            return result_num
        if result_num >= 2 ** 31:
            return 2 ** 31 - 1
        if result_num < - 2 ** 31:
            return -2 ** 31
        return result_num


input_str = "+-1"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)

input_str = "2147483648"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)

input_str = "-000000000000001"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)


input_str = "00000-42a1234"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)


input_str = "words and 987"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)


input_str = "-91283472332"
print(input_str)
solution_test = Solution()
result = solution_test.myAtoi(input_str)
print(result)
