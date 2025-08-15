"""
Graph algorithms with an explicit stack:
- Iterative DFS (with discovery/finish timestamps)
- Topological sort using an explicit stack (DFS variant)
Shows how to replace recursion and keep control over memory/stack depth.
"""
from __future__ import annotations
from typing import Dict, List

def iterative_dfs(graph: Dict[int, List[int]], s: int):
    time = 0
    disc, fini = {}, {}
    st = [(s, 0)]  # (node, next_child_index)
    seen = {s}
    order = []
    while st:
        u, idx = st[-1]
        if idx == 0:
            disc[u] = time; time += 1
            order.append(u)
        if idx < len(graph.get(u, [])):
            v = graph[u][idx]
            st[-1] = (u, idx+1)
            if v not in seen:
                seen.add(v)
                st.append((v, 0))
        else:
            fini[u] = time; time += 1
            st.pop()
    return order, disc, fini

def topo_sort_dfs(graph: Dict[int, List[int]]):
    seen = set()
    out = []
    for s in graph:
        if s in seen: continue
        st = [(s, 0)]
        while st:
            u, i = st[-1]
            if u not in seen:
                seen.add(u)
            if i < len(graph.get(u, [])):
                v = graph[u][i]
                st[-1] = (u, i+1)
                if v not in seen:
                    st.append((v, 0))
            else:
                out.append(u)
                st.pop()
    out.reverse()
    return out

def _demo():
    g = {
        0:[1,2],
        1:[3],
        2:[3,4],
        3:[5],
        4:[5],
        5:[]
    }
    order, disc, fini = iterative_dfs(g, 0)
    print("DFS order:", order)
    print("disc times:", disc)
    print("fini times:", fini)
    print("Topo sort:", topo_sort_dfs(g))

if __name__ == "__main__":
    _demo()
