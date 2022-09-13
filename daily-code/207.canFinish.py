import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = {}
        visited = [0] * numCourses
        result = []
        valid = True
        for item in prerequisites:
            item_1 = item[1]
            item_0 = item[0]
            if item_1 not in edges:
                edges[item_1] = []
            edges[item_1].append(item_0)
        
        def dfs(u):
            nonlocal valid
            visited[u] = 1
            
            


numCourses = 2
prerequisites = [[1, 0]]
result = Solution().canFinish(numCourses, prerequisites)
print(f"result:{result}")
