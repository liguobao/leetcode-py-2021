import json


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):

    def __init__(self, seq):
        self.root = None
        self.parse_array_to_tree(seq)

    # 层次遍历来还原
    def parse_array_to_tree(self, seq):
        if len(seq) == 0:
            return None
        self.root = TreeNode(seq[0])
        # 初始化队列数值，先把root扔进去
        queueNode = [self.root]
        tree_index = 0
        seq_index = 1
        seq_len = len(seq)
        # 开始遍历数据
        while(seq_index < seq_len):
            # 当前节点
            current_node = queueNode[tree_index]
            # 下一个nodeIndex
            tree_index = tree_index+1
            # 取一个值，如果不是None，扔到左节点，
            seq_value_left = seq[seq_index]
            # 这里 + 1，为下一个右节点先准备数据
            seq_index = seq_index + 1
            if seq_value_left is not None:
                left_node = TreeNode(seq_value_left)
                current_node.left = left_node
                queueNode.append(left_node)

            if seq_index >= seq_len:
                break
            # 取一个值，如果不是None，扔到右节点
            seq_value_right = seq[seq_index]
            # 继续加+1，等于一次循环拿走两个值，放到当前node下面
            seq_index = seq_index + 1
            if seq_value_right is not None:
                right_node = TreeNode(seq_value_right)
                current_node.right = right_node
                queueNode.append(right_node)
        return self.root

    def toQueue(self, tree_node):
        if tree_node is None:
            return []
        queue_node = [tree_node.val]
        if tree_node.left is not None:
            queue_node = queue_node + self.toQueue(tree_node.left)
        if tree_node.right is not None:
            queue_node = queue_node + self.toQueue(tree_node.right)
        return queue_node

    def toQueueArray(self):
        queueNode = []
        if self.root is None:
            return json.dumps(queueNode)
        queueNode = self.toQueue(self.root)
        return json.dumps(queueNode)

    def __str__(self):
        return self.toQueueArray()
