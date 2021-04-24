# -*- coding: utf-8 -*-

from collections import OrderedDict


class LRUCache(OrderedDict):
    '''不能存储可变类型对象，不能并发访问set()'''

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        value = self.cache.get(key)
        if value:
            self.cache.move_to_end(key)
        return value

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # pop出第一个item
        self.cache[key] = value  # 设置值
