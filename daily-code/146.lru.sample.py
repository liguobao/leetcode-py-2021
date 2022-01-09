class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
# https://leetcode-cn.com/problems/lru-cache/


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key, c_val=None):
        move_item: ListNode = self.hashmap[key]
        # 先将需要移动的节点前后都处理掉
        move_item.prev.next = move_item.next
        move_item.next.prev = move_item.prev

        # 把当前节点放到最后

        last_node: ListNode = self.tail.prev
        last_node.next = move_item
        move_item.prev = last_node
        
        self.tail.prev = move_item
        move_item.next = self.tail
        if c_val:
            move_item.val = c_val

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            self.move_to_tail(key)
            return self.hashmap[key].val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            self.move_to_tail(key,c_val= value)
            return
        if len(self.hashmap) == self.capacity:
            old_first_node:ListNode = self.head.next
            self.head.next = old_first_node.next
            old_first_node.next.prev = self.head
            self.hashmap.pop(old_first_node.key)
        new_node = ListNode(key=key,val=value)
        self.hashmap[key] = new_node
        last_node:ListNode = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node
        new_node.next = self.tail
        


# Your LRUCache object will be instantiated and called as such:
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
