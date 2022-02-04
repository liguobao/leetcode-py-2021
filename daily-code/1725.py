
# https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# 给你一个数组 rectangles ，其中 rectangles[i] = [li, wi] 表示第 i 个矩形的长度为 li 、宽度为 wi 。
# 如果存在 k 同时满足 k <= li 和 k <= wi ，就可以将第 i 个矩形切成边长为 k 的正方形。例如，矩形 [4,6] 可以切成边长最大为 4 的正方形。
# 设 maxLen 为可以从矩形数组 rectangles 切分得到的 最大正方形 的边长。
# 请你统计有多少个矩形能够切出边长为 maxLen 的正方形，并返回矩形 数目 。

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # 存储所有矩形变成正方形的边长字典，
        rectangle_dict = {}
        for item in rectangles:
            # 短边为正方形的边长
            min_value = min(item)
            if min_value not in rectangle_dict:
                rectangle_dict[min_value] =0 
            rectangle_dict[min_value] = rectangle_dict[min_value] +1  
        # 获取最长正方形边长
        max_key= sorted(rectangle_dict.keys())[-1]
        # 返回数量即可
        return rectangle_dict[max_key]


rectangles = [[5,8],[3,9],[5,12],[16,5]]
result = Solution().countGoodRectangles(rectangles)
print(f"rectangles:{rectangles},result:{result}")


rectangles = [[2,3],[3,7],[4,3],[3,7]]
result = Solution().countGoodRectangles(rectangles)
print(f"rectangles:{rectangles},result:{result}")
