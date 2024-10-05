class Stack:

    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def empty(self):
        return len(self._data) == 0

class StackMin:

    def __init__(self):
        self._stack = Stack()

    def peek(self):
        return self._stack.peek()[0]

    def get_minimum(self):
        return self._stack.peek()[1]

    def pop(self):
        return self._stack.pop()[0]

    def push(self, item):
        mi = item if self._stack.empty() else min(self._stack.peek()[1], item)
        self._stack.push((item, mi))

    def empty(self):
        return self._stack.empty()
