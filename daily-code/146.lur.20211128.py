class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev: ListNode = None
        self.next: ListNode = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.capacity = capacity
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int):
        if key in self.hashmap:
            self.move_to_tail(key)
        cache_node = self.hashmap.get(key, None)
        return cache_node.val if cache_node else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key, value)
            return
        # 数量满了，移除第一个元素
        if len(self.hashmap) == self.capacity:
            # hashmap中移除头部
            old_first_node = self.head.next
            self.hashmap.pop(old_first_node.key)
            # 当前第一个元素 为 old_first_node.next
            current_first_node = old_first_node.next
            self.head.next = current_first_node
            current_first_node.prev = self.head
        current_node =ListNode(key, value)
        self.hashmap[key] = current_node
        last_node = self.tail.prev
        last_node.next = current_node
        current_node.prev = last_node
        current_node.next = self.tail
        self.tail.prev = current_node

    def move_to_tail(self, key, c_val=None):
        """把节点移到尾部（头部的数据先被淘汰）

        Args:
            key ([type]): [description]
        """
        key_node: ListNode = self.hashmap[key]
        # 当前节点抽离走前，设置好当前节点的前后信息
        key_node.prev.next = key_node.next
        key_node.next.prev = key_node.prev
        
        # 插入到tail节点前，设置当前节点的前后信息
        key_node.next = self.tail # 当前节点的下一个是tail节点
        key_node.prev = self.tail.prev # 当前节点的前一个是tail节点原来的前一个元素
        
        self.tail.prev.next = key_node # 设置尾部节点的前一个元素的下一个为当前节点
        self.tail.prev = key_node # 设置尾部节点前一个元素为当前节点
        if c_val:
            key_node.val = c_val
        return


# Your LRUCache object will be instantiated and called as such:
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
