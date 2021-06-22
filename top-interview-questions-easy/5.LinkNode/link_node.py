

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        current_node = self
        array = []
        while(True):
            if not current_node:
                break
            array.append(current_node.val)
            current_node = current_node.next
        return str(array)


def arrayToLinkNode(array):
    if len(array) == 0:
        return None
    first_node = ListNode(array[0])
    p_node = first_node
    for item in array[1:]:
        current_node = ListNode(item)
        p_node.next = current_node
        p_node = current_node
    return first_node


link_array = [4, 5, 1, 9]
first_node = arrayToLinkNode(link_array)
