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
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.move_to_tail(key)
        c_node:ListNode = self.hashmap.get(key, None)
        return c_node.val if c_node else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key, value)
            return
        if len(self.hashmap) == self.capacity:
            first_node: ListNode = self.head.next
            # 从Hashmap中移除节点
            self.hashmap.pop(first_node.key)
            # 切换掉第一个节点前后数据
            first_node.next.prev = self.head
            self.head.next = first_node.next
        new_node = ListNode(key=key, val=value)
        self.hashmap[key] = new_node
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node
        new_node.next = self.tail
       

    def move_to_tail(self, key, current_val=None):
        move_node: ListNode = self.hashmap[key]
        if current_val:
            move_node.val = current_val
        # 抽离当前元素
        prev_node = move_node.prev
        prev_node.next = move_node.next
        move_node.next.prev = prev_node

        # 把当前元素放到队尾
        self.tail.prev.next = move_node
        move_node.prev = self.tail.prev
        move_node.next = self.tail
        self.tail.prev = move_node


# Your LRUCache object will be instantiated and called as such:
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
