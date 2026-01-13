class myStack:
    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top = -1

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size - 1

    def push(self, x):
        if not self.isFull():
            self.top += 1
            self.arr[self.top] = x

    def pop(self):
        if not self.isEmpty():
            self.top -= 1

    def peek(self):
        if self.isEmpty():
            return -1
        return self.arr[self.top]
