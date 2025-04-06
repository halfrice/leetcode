# https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import choice


class RandomizedSet:
    def __init__(self):
        self.index_hash = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.index_hash:
            return False

        self.index_hash[val] = len(self.values)
        self.values.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_hash:
            return False

        index_to_remove = self.index_hash[val]
        last_element = self.values[-1]
        self.values[index_to_remove] = last_element
        self.index_hash[last_element] = index_to_remove
        self.values.pop()
        del self.index_hash[val]

        return True

    def getRandom(self) -> int:
        return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


class Utils:
    def __init__(self):
        self.obj = RandomizedSet()

    def command(self, commands):
        res = []

        for c in commands:
            func = c[0]
            val = c[1]

            if func == 'RandomizedSet':
                res.append(None)
            else:
                f = getattr(self.obj, func)
                v = val[0] if val else None
                r = f(v) if v is not None else f()
                res.append(r)

        return res
