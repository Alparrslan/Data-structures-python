"""
Stack implemented using two queues (amortized O(1) for push, O(n) for pop-or-push depending on strategy).
Educational: demonstrates duality between stacks and queues.
"""
from __future__ import annotations
from collections import deque

class StackViaQueues:
    def __init__(self):
        self.q1, self.q2 = deque(), deque()

    def push(self, x):
        # Strategy A: cost on push so that pop is O(1)
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1: raise IndexError("empty")
        return self.q1.popleft()

    def peek(self):
        if not self.q1: raise IndexError("empty")
        return self.q1[0]

def _demo():
    s = StackViaQueues()
    for i in range(5):
        s.push(i)
    print("peek:", s.peek())
    print("pop sequence:", [s.pop() for _ in range(5)])

if __name__ == "__main__":
    _demo()
