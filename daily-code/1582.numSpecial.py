class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        num_result = 0

        row_index = [x for x in range(0, len(mat))]
        column_index = [x for x in range(0, len(mat[0]))]

        def check_i_j(i, j):
            print(f"i:{i},j:{j}")
            rows = mat[i]
            for x in column_index:
                if x != j and rows[x] != 0:
                    return False
            for x in row_index:
                if x != i and mat[x][j] != 0:
                    return False
            return True

        for i in row_index:
            for j in column_index:
                if mat[i][j] == 1:
                    if check_i_j(i, j):
                        num_result = num_result + 1

        return num_result


mat = [[0,0],[0,0],[1,0]]
result = Solution().numSpecial(mat)
print(result)
