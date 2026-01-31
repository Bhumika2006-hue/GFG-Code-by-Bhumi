class kQueues:
    def __init__(self, n, k):
        self.n = n
        self.k = k
        
        self.arr = [0] * n
        self.front = [-1] * k
        self.rear = [-1] * k
        self.next = list(range(1, n)) + [-1]
        
        self.free = 0   # beginning of free list

    def isFull(self):
        return self.free == -1

    def isEmpty(self, i):
        return self.front[i] == -1

    def enqueue(self, x, i):
        if self.isFull():
            return
        
        # Take a free index
        index = self.free
        self.free = self.next[index]
        
        # If queue is empty
        if self.front[i] == -1:
            self.front[i] = index
        else:
            self.next[self.rear[i]] = index
        
        self.next[index] = -1
        self.rear[i] = index
        self.arr[index] = x

    def dequeue(self, i):
        if self.isEmpty(i):
            return -1
        
        index = self.front[i]
        self.front[i] = self.next[index]
        
        # If queue becomes empty
        if self.front[i] == -1:
            self.rear[i] = -1
        
        # Add index back to free list
        self.next[index] = self.free
        self.free = index
        
        return self.arr[index]
