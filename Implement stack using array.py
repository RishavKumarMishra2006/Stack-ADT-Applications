class StackArray:
    def __init__(self, capacity=10**5):
        self.a = []
        self.cap = capacity

    def push(self, x):
        if len(self.a) >= self.cap:
            raise IndexError("Stack overflow")
        self.a.append(x)

    def pop(self):
        if not self.a:
            raise IndexError("Stack underflow")
        return self.a.pop()

    def peek(self):
        if not self.a:
            raise IndexError("Empty stack")
        return self.a[-1]

    def is_empty(self):
        return not self.a

    def size(self):
        return len(self.a)
