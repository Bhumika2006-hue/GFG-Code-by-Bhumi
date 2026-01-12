from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # Dummy head and tail to simplify adding/removing nodes
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        # Add node to the front (most recent)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def pop_tail(self):
        if self.size == 0:
            return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.size = 0
        self.min_freq = 0
        self.key_map = {} # key -> Node
        self.freq_map = defaultdict(DoublyLinkedList) # freq -> DoublyLinkedList

    def _update_freq(self, node):
        # Remove node from its current frequency list
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        # If the current freq list is empty and it was the min_freq, increment min_freq
        if freq == self.min_freq and self.freq_map[freq].size == 0:
            self.min_freq += 1
            
        # Increment node freq and add to the new freq list
        node.freq += 1
        self.freq_map[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1
        node = self.key_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return

        if key in self.key_map:
            node = self.key_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size >= self.cap:
                # Evict the LRU node from the min_freq list
                evict_node = self.freq_map[self.min_freq].pop_tail()
                del self.key_map[evict_node.key]
                self.size -= 1
            
            # Create new node
            new_node = Node(key, value)
            self.key_map[key] = new_node
            self.freq_map[1].add_node(new_node)
            self.min_freq = 1
            self.size += 1