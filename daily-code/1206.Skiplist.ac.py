from random import randint

class Node:
    def __init__(self, val):
        self.val = val
        self.right, self.down = None, None

class Skiplist:
    def __init__(self):
        self.heads = [Node(float("-inf")) for _ in range(16)]
        self.tails = [Node(float("inf")) for _ in range(16)]
        for h, t in zip(self.heads, self.tails): h.right = t
        for up, down in zip(self.heads, self.heads[1:]): up.down = down

    # 搜索其实很简单
    # 在两者之间就到下面去找
    # 比右边还大就去右边找
    # 由于 tail 设置了最大值所以就不会超过 tail
    def search(self, target):
        cur = self.heads[0]
        while cur:
            if cur.val < target <= cur.right.val:
                if target == cur.right.val: return True
                cur = cur.down
            else:
                cur = cur.right
        return False

    def add(self, num):
        s, cur = [], self.heads[0]
        while cur:
            if cur.val < num <= cur.right.val:
                s.append(cur)
                cur = cur.down
            else:
                cur = cur.right
        prev = None
        # 栈记录每次向下的值
        # 只需要在这些节点后插入就可
        # 最后判断是不是需要继续向上建立索引
        while s:
            cur, node = s.pop(), Node(num)
            node.down, node.right = prev, cur.right
            cur.right = node
            prev = node
            if randint(0, 1): break

    # 与搜索类似
    def erase(self, num):
        cur, f = self.heads[0], False
        while cur:
            if cur.val < num <= cur.right.val:
                if num == cur.right.val:
                    cur.right = cur.right.right
                    f = True
                cur = cur.down
            else:
                cur = cur.right
        return f        
