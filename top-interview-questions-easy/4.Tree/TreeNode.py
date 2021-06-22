class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = right


class Tree(object):

    def __init__(self, val_array):
        self.root = None
        array_len = len(val_array)
        if array_len <= 0:
            return
        self.root = TreeNode(val_array[0])
        stack_node = [self.root]
        array_index = 1
        stack_index = 0
        while array_index < array_len:
            current_node = stack_node[stack_index]
            stack_index = stack_index+1
            left_val = val_array[array_index]
            array_index = array_index+1
            if left_val:
                left_node = TreeNode(left_val)
                current_node.left = left_node
                stack_node.append(left_node)
            if array_index >= array_len:
                break
            right_val = val_array[array_index]
            array_index = array_index+1
            if right_val:
                right_node = TreeNode(right_val)
                current_node.right = right_node
                stack_node.append(right_node)
        return


tree = Tree([1, 2, 3, None, None, 4, 5])
print(tree)
