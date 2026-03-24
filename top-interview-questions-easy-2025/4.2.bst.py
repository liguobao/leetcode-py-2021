class Solution(object):
    
    def isValidBST(self, root):
        prev_val = -2 ** 32
        stack_nodes = []
        current_node = root
        while current_node or stack_nodes:
            while current_node:
                stack_nodes.append(current_node)
                current_node = current_node.left
            current_node = stack_nodes.pop()
            if current_node.val <= prev_val:
                return False
            prev_val =current_node.val
            current_node = current_node.right
        return True