"""
Monotonic stack patterns with three classical problems:
1) Next Greater Element (circular variant)
2) Daily Temperatures
3) Largest Rectangle in Histogram
All solved in O(n) using a decreasing/increasing stack as appropriate.
"""
from __future__ import annotations
from typing import List

def next_greater_elements_circular(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [-1]*n
    st = []  # indices, values decreasing
    for i in range(2*n):
        while st and nums[st[-1]] < nums[i % n]:
            ans[st.pop()] = nums[i % n]
        if i < n:
            st.append(i)
    return ans

def daily_temperatures(T: List[int]) -> List[int]:
    ans = [0]*len(T)
    st = []  # indices with decreasing temperatures
    for i, t in enumerate(T):
        while st and T[st[-1]] < t:
            j = st.pop()
            ans[j] = i - j
        st.append(i)
    return ans

def largest_rectangle_area(heights: List[int]) -> int:
    # classic: append sentinel 0 to flush the stack
    st = []
    max_area = 0
    for i, h in enumerate(heights + [0]):
        start = i
        while st and st[-1][1] > h:
            idx, hh = st.pop()
            max_area = max(max_area, hh * (i - idx))
            start = idx
        st.append((start, h))
    return max_area

def _demo():
    print("Next greater (circular):", next_greater_elements_circular([2,1,2,4,3]))
    print("Daily temperatures:", daily_temperatures([73,74,75,71,69,72,76,73]))
    print("Largest rectangle area:", largest_rectangle_area([2,1,5,6,2,3]))

if __name__ == "__main__":
    _demo()
