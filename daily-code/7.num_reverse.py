class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        less_than_zore = x < 0
        input_x = -x if less_than_zore else x
        output_x = 0
        while input_x != 0:
            # 每次把当前的值*10，达到倒过来存储的效果
            # 1234 第一次output =4，第二次 40，第三次 400，第四次 4000
            output_x = output_x * 10
            end_num = input_x % 10
            input_x = int(input_x / 10)
            output_x = output_x + end_num
        output_x = -output_x if less_than_zore else output_x
        if output_x < - 2 ** 31 or output_x > 2 ** 31:
            return 0
        return output_x
