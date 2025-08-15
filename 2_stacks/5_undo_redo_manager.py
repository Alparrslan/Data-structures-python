"""
Undo/Redo manager using two stacks.
- `do(action, inverse)` records forward and inverse operations.
- `undo()` and `redo()` execute the right functions.
This pattern underpins editors, spreadsheets, and CAD tools.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Command:
    do: callable
    undo: callable
    desc: str

class UndoRedo:
    def __init__(self):
        self._done: list[Command] = []
        self._undone: list[Command] = []

    def apply(self, cmd: Command) -> None:
        cmd.do()
        self._done.append(cmd)
        self._undone.clear()

    def undo(self) -> None:
        if not self._done: raise RuntimeError("nothing to undo")
        cmd = self._done.pop()
        cmd.undo()
        self._undone.append(cmd)

    def redo(self) -> None:
        if not self._undone: raise RuntimeError("nothing to redo")
        cmd = self._undone.pop()
        cmd.do()
        self._done.append(cmd)

def _demo():
    text: list[str] = []  # emulate a rope/GapBuffer with a simple list for demo
    mgr = UndoRedo()

    def insert(pos: int, ch: str):
        return Command(
            do=lambda: text.insert(pos, ch),
            undo=lambda: text.pop(pos),
            desc=f"insert '{ch}' at {pos}",
        )

    mgr.apply(insert(0,"H")); mgr.apply(insert(1,"i")); mgr.apply(insert(2,"!"))
    print("text:", "".join(text))
    mgr.undo(); print("after undo:", "".join(text))
    mgr.redo(); print("after redo:", "".join(text))

if __name__ == "__main__":
    _demo()
