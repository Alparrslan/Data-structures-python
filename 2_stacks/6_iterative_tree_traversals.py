"""
Iterative binary-tree traversals using an explicit stack.
- preorder, inorder, postorder (one-stack version using last-visited pointer)
Also includes a succinct helper to build a tree from a level-order array.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    val: int
    left: Optional['Node']=None
    right: Optional['Node']=None

def build_tree(level: List[Optional[int]]) -> Optional[Node]:
    if not level: return None
    it = iter(level)
    root = Node(next(it))
    q = [root]
    for a,b in zip(it, it):
        cur = q.pop(0)
        if a is not None:
            cur.left = Node(a); q.append(cur.left)
        if b is not None:
            cur.right = Node(b); q.append(cur.right)
    return root

def preorder(root: Optional[Node]) -> List[int]:
    if not root: return []
    st, out = [root], []
    while st:
        node = st.pop()
        out.append(node.val)
        if node.right: st.append(node.right)
        if node.left: st.append(node.left)
    return out

def inorder(root: Optional[Node]) -> List[int]:
    out, st, cur = [], [], root
    while cur or st:
        while cur:
            st.append(cur); cur = cur.left
        cur = st.pop(); out.append(cur.val); cur = cur.right
    return out

def postorder(root: Optional[Node]) -> List[int]:
    out, st = [], []
    last = None
    cur = root
    while cur or st:
        if cur:
            st.append(cur); cur = cur.left
        else:
            peek = st[-1]
            if peek.right and last is not peek.right:
                cur = peek.right
            else:
                out.append(peek.val)
                last = st.pop()
    return out

def _demo():
    root = build_tree([1,2,3,4,5,6,7,None,None,8,9])
    print("preorder:", preorder(root))
    print("inorder:", inorder(root))
    print("postorder:", postorder(root))

if __name__ == "__main__":
    _demo()
