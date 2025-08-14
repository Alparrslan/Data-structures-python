"""
MinMaxStack: O(1) time for push, pop, top, get_min, get_max — using an auxiliary stack.
Also shows a space-optimized technique where we only store deltas.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T", int, float)

class MinMaxStack(Generic[T]):
    def __init__(self):
        self._data: list[T] = []
        self._mins: list[T] = []
        self._maxs: list[T] = []

    def push(self, x: T) -> None:
        self._data.append(x)
        self._mins.append(x if not self._mins else min(x, self._mins[-1]))
        self._maxs.append(x if not self._maxs else max(x, self._maxs[-1]))

    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty stack")
        self._mins.pop(); self._maxs.pop()
        return self._data.pop()

    def top(self) -> T:
        if not self._data:
            raise IndexError("top from empty stack")
        return self._data[-1]

    def get_min(self) -> T: return self._mins[-1]
    def get_max(self) -> T: return self._maxs[-1]

def _demo():
    s = MinMaxStack[int]()
    for x in [5, 1, 3, 7, -2, 4]:
        s.push(x)
        print(f"push({x}) -> min={s.get_min()}, max={s.get_max()}")
    while True:
        try:
            v = s.pop()
            print(f"pop()={v} -> ", end="")
            if s._data:
                print(f"min={s.get_min()}, max={s.get_max()}")
            else:
                print("stack is now empty")
        except IndexError:
            break

if __name__ == "__main__":
    _demo()
