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

    def get(self, key: int):
        if key in self.hashmap:
            self.move_to_tail(key)
            
        c_node: ListNode = self.hashmap.get(key, None)
        return c_node.val if c_node else -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.move_to_tail(key, value)
            return
        if len(self.hashmap) == self.capacity:
            first_node = self.head.next
            self.hashmap.pop(first_node.key)
            self.head.next = first_node.next
            first_node.next.prev = self.head
        new_node = ListNode(key=key,val=value)
        self.hashmap[key] = new_node
        last_node = self.tail.prev
        last_node.next = new_node
        new_node.prev = last_node
        self.tail.prev = new_node
        new_node.next = self.tail
        

    def move_to_tail(self, key, c_val=None):
        """把节点移到尾部（头部的数据先被淘汰）
        Args:
            key ([type]): [description]
        """
        move_node:ListNode = self.hashmap[key]
        # 移除当前节点的前后关联
        move_node.next.prev = move_node.prev
        move_node.prev.next = move_node.next
       
        
        # 先把最后一个节点拿出来
        last_node = self.tail.prev
        # 设置当前最后节点的下一个节点为新节点
        last_node.next = move_node
        move_node.prev = last_node
        
        # 设置新节点和尾结点的关系
        self.tail.prev = move_node
        move_node.next = self.tail
        if c_val:
            move_node.val = c_val
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
