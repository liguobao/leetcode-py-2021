class Solution(object):
    # 找最大值所在的Index，靠后优先
    def find_max_index(self, nums, max_num):
        max_index = nums.index(max_num)
        for i in range(max_index, len(nums)):
            if nums[i] == max_num:
                max_index = i
        return max_index

    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        nums = [x for x in str(num)]
        # 题目限制只能交换一次，本质上只需要把数组中数字最大的放第一位即可
        # 所以只需要找到符合要求的子串交换一次数字即可
        for i in range(len(nums)):
            sub_nums = nums[i:]
            # 获取子串最大值
            max_n = max(sub_nums)
            # 最大值最靠右的位置
            max_index = self.find_max_index(sub_nums, max_n)
            # 边界条件：最大值所在位置不是首位 且 首位数字不是最大值
            # case 98368中 “8368”，不把前后的8换掉，要继续下一个子串
            if max_index != 0 and sub_nums[0] != max_n:
                first_num = sub_nums[0]
                sub_nums[0] = max_n
                sub_nums[max_index] = first_num
                left_nums = nums[:i]
                return int("".join(left_nums+sub_nums))
        return int("".join(nums))


input_num = 98368
result = Solution().maximumSwap(input_num)
print(f"input_num:{input_num},result:{result}")
