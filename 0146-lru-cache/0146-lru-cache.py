# Time Complexity for put and get: O(1)
# Space Complexity: O(N), N = cache len
# https://www.youtube.com/watch?v=7ABFKPK2hD4

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = dict()
        # Maintain left and right pointers for a doubly linked list
        # left = LRU, right = MRU
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):
        prev_node, next_node = node.prev, node.next
        prev_node.next, next_node.prev = next_node, prev_node
        del node
    
    def insert_at_right(self, node):
        prev_node, next_node = self.right.prev, self.right
        prev_node.next = next_node.prev = node
        node.next, node.prev = next_node, prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            curr_node = self.cache[key]
            # Update the LRU linked list
            # Set the searched key to MRU by removing and inserting
            self.remove(curr_node)
            self.insert_at_right(curr_node)
            return curr_node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove the existing node
            curr_node = self.cache[key]
            self.remove(curr_node)
        new_node = Node(key, value)
        self.insert_at_right(new_node)
        self.cache[key] = new_node

        # Check if cache is out of bounds
        if len(self.cache) > self.cap:
            # Remove LRU
            lru_node = self.left.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)