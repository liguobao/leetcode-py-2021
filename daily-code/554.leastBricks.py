# https://leetcode-cn.com/problems/brick-wall/
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        height = len(wall)
        if height ==0:
            return 0
        width = len(wall[0])
        # 维护了每个缝隙出现过的数量
        wall_dis_map = {}
        for one_row in wall:
            _dis = 0
            for brick in one_row[:-1]:
                _dis = _dis + brick
                if _dis not in wall_dis_map:
                    wall_dis_map[_dis] = 1
                else:
                    wall_dis_map[_dis] =  wall_dis_map[_dis] +1
        if wall_dis_map:
             max_cnt = max(wall_dis_map.values())
             return height - max_cnt
        else:
            return height


solution = Solution()
wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
result = solution.leastBricks(wall)
print(result)

wall =  [[1],[1],[1]]
result = solution.leastBricks(wall)
print(result)
