# (C) Albert Mietus, 2026. Part of Castle/CCastle project

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("stack is empty, can't pop")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty, can't peek")
        return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)
    __len__ = size # GAM: Don't know what I prefer as api: `stack.size()` of `len(stack)`

