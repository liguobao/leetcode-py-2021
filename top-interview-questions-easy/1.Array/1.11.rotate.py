class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return
        matrix_n = len(matrix[0])
        # 旋转层数，index_i 第几层
        for index_i in range(0, int((matrix_n+1)/2)):
            # index_j 每层的起始位置
            for index_j in range(index_i, matrix_n - index_i - 1):
                item_value = matrix[index_i][index_j]
                # 第几行的第j个元素
                m = matrix_n - index_j - 1
                # 第几列的第i个元素
                n = matrix_n - index_i - 1
                matrix[index_i][index_j] = matrix[m][index_i]
                matrix[m][index_i] = matrix[n][m]
                matrix[n][m] = matrix[index_j][n]
                matrix[index_j][n] = item_value


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution_test = Solution()
result = solution_test.rotate(board)
