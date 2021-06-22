
class MiQueue:

    def __init__(self):
        self.left = []
        self.right = []

    def push(self, val):
        self.left.append(val)

    def pop(self):
        self.right = []
        c_val = None
        while self.left:
            c_val = self.left.pop()
            self.right.append(c_val)
        while self.right:
            r_val = self.right.pop()
            self.left.append(r_val)
        self.left.remove(c_val)
        return c_val


miQueue = MiQueue()

miQueue.push(1)
miQueue.push(2)
miQueue.push(3)
print(miQueue.pop())
print(miQueue.pop())
print(miQueue.pop())
