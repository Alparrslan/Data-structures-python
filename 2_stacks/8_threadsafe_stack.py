"""
Thread-safe stack using a lock and condition variable.
Demonstrates producers/consumers pushing/popping concurrently without races.
Note: CPython's GIL does not make non-atomic operations safe; we still need locks.
"""
from __future__ import annotations
import threading, random, time
from typing import Optional, Generic, TypeVar

T = TypeVar("T")

class ThreadSafeStack(Generic[T]):
    def __init__(self):
        self._data: list[T] = []
        self._cv = threading.Condition()

    def push(self, item: T) -> None:
        with self._cv:
            self._data.append(item)
            self._cv.notify()

    def pop(self, timeout: Optional[float] = None) -> T:
        with self._cv:
            start = time.time()
            while not self._data:
                remaining = None if timeout is None else max(0, timeout - (time.time() - start))
                if timeout is not None and remaining == 0:
                    raise TimeoutError("pop timed out")
                self._cv.wait(timeout=remaining)
            return self._data.pop()

def _demo():
    stk = ThreadSafeStack[int]()
    out = []
    def producer():
        for i in range(10):
            time.sleep(random.random()*0.02)
            stk.push(i)
    def consumer():
        for _ in range(10):
            v = stk.pop(timeout=1.0)
            out.append(v)
    t1 = threading.Thread(target=producer); t2 = threading.Thread(target=consumer)
    t1.start(); t2.start(); t1.join(); t2.join()
    print("popped values (not ordered):", out, "len=", len(out))

if __name__ == "__main__":
    _demo()
