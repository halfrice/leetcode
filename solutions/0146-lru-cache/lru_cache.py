# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.count = 0
        self.left = Node()
        self.right = Node()

        self.left.next = self.right
        self.right.prev = self.left

    def update_cache(self, key):
        cur = self.cache[key]

        # Reattach current node at MRU (Most Recently Used)
        cur.prev = self.right.prev
        self.right.prev.next = cur
        cur.next = self.right
        self.right.prev = cur

    def get(self, key: int) -> int:
        if key in self.cache:
            cur = self.cache[key]

            # Unlink current node and link severed nodes to each other
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # Reattach current node
            self.update_cache(key)

            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # Update key already in cache
        if key in self.cache:
            cur = self.cache[key]

            # Update value of key if it's changed
            if cur.val != value:
                cur.val = value

            # Do nothing if cur is already MRU
            if cur.next == self.right:
                return

            # Unlink current node and link severed nodes to each other
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

            # Reattach current node
            self.update_cache(key)

            return

        # Put new key into cache
        # If adding a new node exceeds the cache's key capacity, remove LRU node
        if self.count + 1 > self.cap:
            del self.cache[self.left.next.key]

            self.left.next = self.left.next.next
            self.left.next.prev = self.left

        # Add key and new node to cache and update count
        self.cache[key] = Node(key, value)
        self.count += 1

        self.update_cache(key)

        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Helper class for running tests
class Utils:
    def __init__(self):
        self.obj = None

    def command(self, commands):
        res = []

        for cmd in commands:
            func = cmd[0]
            val = cmd[1]

            if func == 'LRUCache':
                self.obj = LRUCache(val[0])
                res.append(None)
            else:
                f = getattr(self.obj, func)
                r = f(val[0], val[1]) if len(val) > 1 else f(val[0])
                res.append(r)

        return res
