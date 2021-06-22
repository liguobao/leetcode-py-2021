from random import randint


class SkipNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.down = None


max_level = 16
power = 2


# https://leetcode-cn.com/problems/design-skiplist/solution/1206-she-ji-tiao-biao-pythonshi-xian-by-tuotuoli/

class Skiplist(object):

    def __init__(self):
        # 初始化每一层的左右的正负无穷
        # 左边负无穷，右边正无穷，实现可以不断往下查找的目的
        left_nodes = [SkipNode(-float('inf')) for _ in range(max_level)]
        right_nodes = [SkipNode(float('inf')) for _ in range(max_level)]
        for i in range(max_level-1):
            left_nodes[i].right = right_nodes[i]
            left_nodes[i].down = left_nodes[i+1]
            right_nodes[i].down = right_nodes[i+1]
        # 最后一层单独处理，只有向右指向，没有向下指向
        left_nodes[-1].right = right_nodes[-1]
        # 跳表初始指针为左壁的首元素
        self.head = left_nodes[0]

    def search(self, target):
        """
        :type target: int
        :rtype: bool
        """
        current_node = self.head
        while current_node:
            if current_node.value == target:
                return True
            if current_node.value > target:
                current_node = current_node.down
            else:
                current_node = current_node.right
        return False

    def add_with_timeout(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 保存了需要调整的节点
        prev_nodes = []
        current_node = self.head
        while current_node:
            # 右边大于 当前值，则说明当前值需要往下一层放
            # 这个情况也需要把当前节点的指针保存一起来，调整的时候需要用
            if current_node.right.value >= num:
                prev_nodes.append(current_node)
                current_node = current_node.down
            else:
                current_node = current_node.right
        prev = None
        while prev_nodes:
            cur_node = prev_nodes.pop()
            num_node = SkipNode(num)
            num_node.down = prev
            num_node.right = cur_node.right
            cur_node.right = num_node
            prev = num_node
        pass


    def erase(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ans =False
        current_node = self.head
        while current_node:
            if current_node.right.value > num:
                current_node = current_node.down
            elif current_node.right.value < num:
                current_node = current_node.right
            else:
                ans = True
                current_node.right = current_node.right.right
                current_node = current_node.down
        return ans


# Your Skiplist object will be instantiated and called as such:
obj = Skiplist()
target = 10
obj.add(2)
obj.add(1)
obj.add(3)
obj.add(11)
param_1 = obj.search(target)
print(param_1)
num = 5
obj.add(num)
param_3 = obj.erase(num)
print(param_3)
print(obj.search(5))
