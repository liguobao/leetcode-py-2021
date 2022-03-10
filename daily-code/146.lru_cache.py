class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev: ListNode = None
        self.next: ListNode = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.tail.prev = self.head
        self.head.next = self.tail

    def get(self, key: int):
        if key in self.hashmap:
            self.move_to_tail(key)
        c_node: ListNode = self.hashmap.get(key, None)
        return c_node.val if c_node else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key, value)
            return
        if self.capacity == len(self.hashmap):
            first_node = self.head.next
            self.hashmap.pop(first_node.key)
            self.head.next = first_node.next
            first_node.next.prev = self.head
        new_node = ListNode(key, value)
        self.hashmap[key] = new_node
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def move_to_tail(self, key, c_val=None):
        move_node: ListNode = self.hashmap[key]
        # 抽离当前节点
        prev_node = move_node.prev
        prev_node.next = move_node.next
        move_node.next.prev = prev_node

        # 把当前最后一个节点的下一个节点设置成需要移动的节点
        last_node = self.tail.prev
        last_node.next = move_node
        move_node.prev = last_node

        self.tail.prev = move_node
        move_node.next = self.tail

        # 如果c_val 存在，更新移动节点的值
        if c_val:
            move_node.val = c_val


# Your LRUCache object will be instantiated and called as such:
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
