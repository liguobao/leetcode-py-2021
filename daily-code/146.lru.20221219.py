
class ListNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
# https://leetcode-cn.com/problems/lru-cache/


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.hashmap:
            self.move_to_tail(key)
            return self.hashmap[key].val
        else:
            return -1
        
    def move_to_tail(self, key, c_val=None):
        current_node:ListNode = self.hashmap[key]
        if c_val:
            current_node.val = c_val
        tail_node = self.tail
        ## 处理当前节点的前后关系
        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        tail_node.prev.next = current_node
        current_node.next = tail_node
        
    
    def put(self, key, value):
        if key in self.hashmap:
            self.move_to_tail(key, value)
            return
        if len(self.hashmap) == self.capacity:
            self.hashmap.pop(self.head.next.key)
            self.head.next = self.head.next.next
            self.head.next.prex = self.head
        new_node = ListNode(key, value)
        self.hashmap[key] = new_node
        
        new_node.prev = self.tail.prev
        new_node.next = self.tail
        
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        
        
        
    
    
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
