"""
Shunting-yard algorithm: infix -> postfix (RPN) with support for unary minus and power '^'.
Then evaluate RPN using a stack. Whitespace-agnostic, robust tokenization.
"""
from __future__ import annotations
import re
from typing import List, Iterable

OPS = {
    "+": (1, "L"), "-": (1, "L"),
    "*": (2, "L"), "/": (2, "L"), "%": (2, "L"),
    "^": (3, "R"),
}

def tokenize(expr: str) -> Iterable[str]:
    token_spec = r"""
        \s*(?:
            (?P<number>\d+(?:\.\d+)?) |
            (?P<op>[+\-*/%^]) |
            (?P<lpar>\() |
            (?P<rpar>\))
        )
    """
    for m in re.finditer(token_spec, expr, re.X):
        yield m.group(m.lastgroup)

def infix_to_postfix(expr: str) -> List[str]:
    out, st = [], []
    prev = None
    for tok in tokenize(expr):
        if tok.isdigit() or re.match(r"\d+\.\d+", tok):
            out.append(tok)
            prev = "num"
        elif tok in OPS:
            op = tok
            # Handle unary minus by rewiring as 0 - x
            if op == "-" and (prev is None or prev in {"op","lpar"}):
                out.append("0")
            p1, assoc1 = OPS[op]
            while st and st[-1] in OPS:
                p2, assoc2 = OPS[st[-1]]
                if (assoc1 == "L" and p1 <= p2) or (assoc1 == "R" and p1 < p2):
                    out.append(st.pop())
                else:
                    break
            st.append(op)
            prev = "op"
        elif tok == "(":
            st.append(tok); prev = "lpar"
        elif tok == ")":
            while st and st[-1] != "(":
                out.append(st.pop())
            if not st:
                raise ValueError("Mismatched parentheses")
            st.pop(); prev = "rpar"
        else:
            raise ValueError(f"Invalid token: {tok}")
    while st:
        t = st.pop()
        if t in {"(", ")"}:
            raise ValueError("Mismatched parentheses")
        out.append(t)
    return out

def eval_rpn(tokens: Iterable[str]) -> float:
    st: list[float] = []
    for t in tokens:
        if re.match(r"^\d+(?:\.\d+)?$", t):
            st.append(float(t))
        else:
            b = st.pop(); a = st.pop()
            if t == "+": st.append(a+b)
            elif t == "-": st.append(a-b)
            elif t == "*": st.append(a*b)
            elif t == "/": st.append(a/b)
            elif t == "%": st.append(a % b)
            elif t == "^": st.append(a**b)
            else: raise ValueError(f"Unknown op {t}")
    if len(st) != 1:
        raise ValueError("Invalid RPN expression")
    return st[0]

def _demo():
    exprs = [
        "3 + 4 * 2 / (1 - 5)^2^3",
        "-3 + 2*(5-7)",
        "5 % 2 + 7 * (2 - 3^2)",
    ]
    for e in exprs:
        rpn = infix_to_postfix(e)
        val = eval_rpn(rpn)
        print(e, "=>", " ".join(rpn), "=", val)

if __name__ == "__main__":
    _demo()
