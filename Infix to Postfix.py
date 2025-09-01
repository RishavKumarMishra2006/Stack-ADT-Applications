def infix_to_postfix(expr: str) -> str:
    # tokens may be contiguous (e.g., a+b*c) -> treat letters/digits as operands
    prec = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1}
    right_assoc = {'^'}
    out, st = [], []
    def is_op(c): return c in prec

    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isalnum():
            # read multi-char operands
            j = i
            while j < len(expr) and expr[j].isalnum():
                j += 1
            out.append(expr[i:j])
            i = j
            continue
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()  # pop '('
        elif is_op(c):
            while st and st[-1] != '(' and (
                prec[st[-1]] > prec[c] or
                (prec[st[-1]] == prec[c] and c not in right_assoc)
            ):
                out.append(st.pop())
            st.append(c)
        i += 1

    while st:
        out.append(st.pop())
    return ' '.join(out)
