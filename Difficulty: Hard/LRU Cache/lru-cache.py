class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, cap):
        self.cap = cap
        self.cache = {}  # Stores key -> Node
        
        # Initialize dummy nodes for the doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Detach node from current position in the list."""
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _add_to_tail(self, node):
        """Insert node right before the tail (Most Recently Used)."""
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Move to tail to mark as Most Recently Used
            self._remove(node)
            self._add_to_tail(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            # Update value and move to tail
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_tail(node)
        else:
            if len(self.cache) >= self.cap:
                # Evict the Least Recently Used (node after head)
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]
            
            # Create new node and add to tail
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_tail(new_node)