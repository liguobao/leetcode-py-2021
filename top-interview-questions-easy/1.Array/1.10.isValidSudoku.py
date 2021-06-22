class Solution(object):
    def isValidSudoku(self, board):
        # 把所有需要判断的数组都组合到这里
        all_array = []
        for board_i in range(0, 9):
            # 直接取每一行
            all_array.append(board[board_i])
            # 构建每一列
            one_array = []
            for board_j in range(0, 9):
                one_array.append(board[board_j][board_i])
            all_array.append(one_array)
        # 开始构建3*3数组
        for board_i_3 in range(0, 9, 3):
            one_array = []
            for board_j_3 in range(0, 3):
                one_array = one_array + board[board_j_3][board_i_3:board_i_3+3]
            all_array.append(one_array)
            one_array = []
            for board_j_3 in range(3, 6):
                one_array = one_array + board[board_j_3][board_i_3:board_i_3+3]
            all_array.append(one_array)
            one_array = []
            for board_j_3 in range(6, 9):
                one_array = one_array + board[board_j_3][board_i_3:board_i_3+3]
            all_array.append(one_array)
        for i in range(0, len(all_array)):
            if self.is_valid(all_array[i]) is True:
                continue
            return False
        return True

    # 判断数组序列只包含数字 1-9 和字符 '.'
    def is_valid(self, i_array):
        array_set = {}
        for item in i_array:
            if item == ".":
                continue
            if item in array_set:
                return False
            else:
                array_set[item] = item
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
solution_test = Solution()
result = solution_test.isValidSudoku(board)
print(result)
