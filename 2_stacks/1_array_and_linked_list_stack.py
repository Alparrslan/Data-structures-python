"""
Two production-grade stack implementations:
- ArrayStack (backed by Python list with amortized O(1) push/pop)
- LinkedListStack (singly linked list; predictable O(1) push/pop; no over-allocation)
Includes micro-benchmarks to compare asymptotics and constant factors.
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Generic, Iterable, Iterator, Optional, TypeVar

T = TypeVar("T")

class ArrayStack(Generic[T]):
    __slots__ = ("_data",)
    def __init__(self, items: Optional[Iterable[T]] = None):
        self._data: list[T] = []
        if items:
            self._data.extend(items)
    def push(self, item: T) -> None:
        self._data.append(item)   # amortized O(1)
    def pop(self) -> T:
        if not self._data:
            raise IndexError("pop from empty ArrayStack")
        return self._data.pop()   # amortized O(1)
    def peek(self) -> T:
        if not self._data:
            raise IndexError("peek from empty ArrayStack")
        return self._data[-1]
    def __len__(self) -> int:
        return len(self._data)
    def __bool__(self) -> bool:
        return bool(self._data)
    def __iter__(self) -> Iterator[T]:
        # LIFO iteration without mutating
        for i in range(len(self._data) - 1, -1, -1):
            yield self._data[i]

@dataclass
class _Node(Generic[T]):
    value: T
    next: Optional["_Node[T]"] = None

class LinkedListStack(Generic[T]):
    __slots__ = ("_top", "_size")
    def __init__(self, items: Optional[Iterable[T]] = None):
        self._top: Optional[_Node[T]] = None
        self._size = 0
        if items:
            for x in items:
                self.push(x)
    def push(self, item: T) -> None:
        self._top = _Node(item, self._top)  # O(1)
        self._size += 1
    def pop(self) -> T:
        if self._top is None:
            raise IndexError("pop from empty LinkedListStack")
        node = self._top
        self._top = node.next
        self._size -= 1
        return node.value
    def peek(self) -> T:
        if self._top is None:
            raise IndexError("peek from empty LinkedListStack")
        return self._top.value
    def __len__(self) -> int:
        return self._size
    def __bool__(self) -> bool:
        return self._top is not None
    def __iter__(self) -> Iterator[T]:
        cur = self._top
        while cur:
            yield cur.value
            cur = cur.next

def _demo():
    print("=== ArrayStack vs LinkedListStack ===")
    arr = ArrayStack[int]()
    ll  = LinkedListStack[int]()
    for i in range(5):
        arr.push(i)
        ll.push(i)
    print("ArrayStack peek:", arr.peek())
    print("LinkedListStack peek:", ll.peek())
    print("ArrayStack pop order:", list(arr))
    print("LinkedListStack pop order:", list(ll))

    # Micro-benchmark (very small, just to show shape — not a rigorous perf test)
    import time
    N = 200_000
    start = time.perf_counter()
    for i in range(N):
        arr.push(i)
    while arr:
        arr.pop()
    t_arr = time.perf_counter() - start

    start = time.perf_counter()
    for i in range(N):
        ll.push(i)
    while ll:
        ll.pop()
    t_ll = time.perf_counter() - start
    print(f"Amortized behavior — ArrayStack: {t_arr:.3f}s, LinkedListStack: {t_ll:.3f}s")

if __name__ == "__main__":
    _demo()
