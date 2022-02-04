# 你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，
# 并用大小为 m * n 的网格 grid 进行了标注。
# 每个单元格中的整数就表示这一单元格中的黄金数量；
# 如果该单元格是空的，那么就是 0。

# 为了使收益最大化，矿工需要按以下规则来开采黄金：

# 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
# 矿工每次可以从当前位置向上下左右四个方向走。
# 每个单元格只能被开采（进入）一次。
# 不得开采（进入）黄金数目为 0 的单元格。
# 矿工可以从网格中 任意一个 有黄金的单元格出发或者是停止。

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/path-with-maximum-gold
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_gold_resuls = []
        next_i = 0
        next_j = 0

        def find_gold(i, j, result):
            if check_gold(i, j):
                result.append(grid[i][j])
                i, j = get_max_next_step(i, j)
                if i == -1 and j == -1:
                    return result
                return find_gold(i, j, result)
            return result

        def check_gold(i, j):
            return grid[i][j] != 0

        def get_max_next_step(i, j):
            m = len(grid[0])
            n = len(grid)
            left = grid[i][j-1] if j > 0 else 0
            right = grid[i][j+1] if j+1 < m else 0
            top = grid[i-1][j] if i > 0 else 0
            button = grid[i+1][j] if i+1 < n else 0
            values = {
                left: [i, j-1],
                right: [i, j+1],
                top: [i-1, j],
                button: [i+1, j]
            }
            max_value = sorted(values.keys())[-1]
            if max_value == 0:
                return -1, -1
            # 最大值所在的位置
            return values[max_value]


grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
result = Solution().getMaximumGold(grid)
print(f"grid:{grid},result:{result}")
