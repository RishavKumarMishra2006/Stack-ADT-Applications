def eval_postfix(tokens) -> int:
    """
    tokens: iterable of tokens e.g. ["2","1","+","3","*"] or "2 1 + 3 *".split()
    Supports integers and operators + - * / ^.
    Division is integer trunc toward zero (like GFG/HackerRank).
    """
    if isinstance(tokens, str):
        tokens = tokens.split()
    st = []
    import math
    for t in tokens:
        if t.lstrip('-').isdigit():
            st.append(int(t))
        else:
            b = st.pop(); a = st.pop()
            if t == '+': st.append(a + b)
            elif t == '-': st.append(a - b)
            elif t == '*': st.append(a * b)
            elif t == '/': st.append(int(a / b))  # trunc toward zero
            elif t == '^': st.append(a ** b)
            else: raise ValueError("Unknown op")
    return st[-1]
