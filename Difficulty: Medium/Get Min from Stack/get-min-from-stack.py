class SpecialStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[-1]))

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.minStack.pop()

    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def getMin(self):
        if not self.minStack:
            return -1
        return self.minStack[-1]
