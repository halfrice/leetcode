# https://leetcode.com/problems/min-stack/


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mval = self.stack[-1][1] if self.stack else float('inf')
        self.stack.append([val, min(val, mval)])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Runs test cases using an instance of MinStack
class Runner:
    def __init__(self):
        self.min_stack = MinStack()

    def run(self, ops, vals):
        self.ops = ops
        self.vals = vals
        r = []
        for i, c in enumerate(self.ops):
            if c == 'MinStack':
                r.append(None)
            else:
                f = getattr(self.min_stack, c)
                v = vals[i][0] if vals[i] else None
                res = f(v) if v is not None else f()
                r.append(res)
        return r
