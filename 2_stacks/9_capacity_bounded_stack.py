"""
Capacity-bounded stack with configurable overflow policy:
- RAISE: raise OverflowError
- DROP_OLDEST: remove bottom-most element before pushing new one
- IGNORE: ignore the new element when full
Useful for fixed-memory systems or bounded history buffers.
"""
from __future__ import annotations
from enum import Enum

class OverflowPolicy(Enum):
    RAISE = 1
    DROP_OLDEST = 2
    IGNORE = 3

class BoundedStack:
    def __init__(self, capacity: int, policy: OverflowPolicy = OverflowPolicy.RAISE):
        assert capacity > 0
        self.capacity = capacity
        self.policy = policy
        self._data: list[int] = []

    def push(self, x: int) -> None:
        if len(self._data) >= self.capacity:
            if self.policy == OverflowPolicy.RAISE:
                raise OverflowError("stack full")
            elif self.policy == OverflowPolicy.DROP_OLDEST:
                # drop bottom-most element (index 0); O(n) but acceptable for small caps
                self._data.pop(0)
            elif self.policy == OverflowPolicy.IGNORE:
                return
        self._data.append(x)

    def pop(self) -> int:
        if not self._data: raise IndexError("empty")
        return self._data.pop()

    def __repr__(self) -> str:
        return f"BoundedStack({self._data}, cap={self.capacity}, policy={self.policy.name})"

def _demo():
    print("-- RAISE --")
    s = BoundedStack(3, OverflowPolicy.RAISE)
    for i in (1,2,3): s.push(i)
    try:
        s.push(4)
    except OverflowError as e:
        print("expected:", e)

    print("-- DROP_OLDEST --")
    s = BoundedStack(3, OverflowPolicy.DROP_OLDEST)
    for i in (10,20,30,40):
        s.push(i); print(s)

    print("-- IGNORE --")
    s = BoundedStack(2, OverflowPolicy.IGNORE)
    for i in (7,8,9):
        s.push(i); print(s)

if __name__ == "__main__":
    _demo()
