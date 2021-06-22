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
        # 初始化 头结点和尾结点
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_to_tail(self, key, c_val):
        key_node = self.hashmap[key]
        # 当前结点的前结点的下一个，配置成当前节点的下一个
        # 当前节点的下一个节点的前结点，配置成当前节点的前一个
        key_node.prev.next = key_node.next
        key_node.next.prev = key_node.prev

        # 将当前元素插到尾部
        # 先修改当前元素的前置为尾部元素前一个，当前元素的后面设置为尾部
        key_node.prev = self.tail.prev
        key_node.next = self.tail
        # 把尾部的前置元素的后一个，设置为当前元素
        # 吧尾部的前置设置成当前
        self.tail.prev.next = key_node
        self.tail.prev = key_node
        if c_val:
            key_node.val = c_val

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            self.move_to_tail(key, None)
        result = self.hashmap.get(key, -1)
        return result if result == -1 else result.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hashmap:
            self.move_to_tail(key, value)
        else:
            if len(self.hashmap) == self.capacity:
                # 删除hashmap里面的头结点元素
                self.hashmap.pop(self.head.next.key)
                # 当前头结点的next设置成next.next
                # 当前头结点的next的前一个元素设置成头
                # 最后实现把首个元素删除掉
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            new_node = ListNode(key, value)
            self.hashmap[key] = new_node
            # 把新节点的前置节点设置为尾部前置
            # 把当前节点的next设置成尾部
            new_node.prev = self.tail.prev
            new_node.next = self.tail
            # 把尾部节点的原始前置节点的next设置成当前节点
            # 把尾部节点的前置节点设置成当前节点
            # 最终实现插入节点
            self.tail.prev.next = new_node
            self.tail.prev = new_node


# Your LRUCache object will be instantiated and called as such:
capacity = 2
lru_cache = LRUCache(capacity)
print(lru_cache.put(2, 1))
print(lru_cache.put(2, 2))
print(lru_cache.get(2))
print(lru_cache.put(1, 1))
print(lru_cache.put(4, 1))
print(lru_cache.get(2))
