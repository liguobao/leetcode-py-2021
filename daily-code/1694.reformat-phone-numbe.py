class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        num_array = []
        for item in number:
            if item == " " or item == "-":
                continue
            num_array.append(item)
        num_count = int((len(num_array) / 3) - 1)
        results = []
        for i in range(num_count):
            results.append("".join(num_array[i*3:i*3+3]))
        last_nums = num_array[num_count * 3:]
        if len(last_nums) == 5:
            results.append("".join(last_nums[:3]))
            results.append("".join(last_nums[3:]))
        elif len(last_nums) == 4:
            results.append("".join(last_nums[:2]))
            results.append("".join(last_nums[2:]))
        elif len(last_nums) <= 3:
            results.append("".join(last_nums))
        return "-".join(results)


numbers = "12"
result = Solution().reformatNumber(numbers)
print(result)
