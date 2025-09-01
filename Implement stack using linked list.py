class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt

class StackLL:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, x):
        self.head = Node(x, self.head)
        self._size += 1

    def pop(self):
        if not self.head:
            raise IndexError("Stack underflow")
        x = self.head.data
        self.head = self.head.next
        self._size -= 1
        return x

    def peek(self):
        if not self.head:
            raise IndexError("Empty stack")
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size
