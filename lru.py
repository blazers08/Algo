from collections import deque


class LRUCache:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.queue = deque()

    def is_queue_full(self):
        return len(self.queue) == self.cache_size

    def set(self, value):
        if value not in self.queue:
            if self.is_queue_full():
                self.queue.pop()
                self.queue.appendleft(value)
            else:
                self.queue.appendleft(value)

    def get(self, value):
        if value not in self.queue:
            return -1
        else:
            self.queue.remove(value)
            self.queue.appendleft(value)
            return self.queue


if __name__ == '__main__':
    # set cache_size to 3
    lru_cache = LRUCache(3)

    lru_cache.set(7)
    lru_cache.set(2)
    lru_cache.set(3)
    print(lru_cache.get(7))
    lru_cache.set(5)
    print(lru_cache.get(5))
