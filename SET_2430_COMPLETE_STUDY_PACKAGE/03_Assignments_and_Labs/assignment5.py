# Assignment 5

# Part A: Browser History

class BrowserHistory:
    def __init__(self, homepage):
        self.curr = homepage
        self.back_stack = []
        self.fwd_stack = []

    def visit(self, url):
        self.back_stack.append(self.curr)
        self.curr = url
        self.fwd_stack.clear()

    def back(self, steps):
        while steps > 0 and self.back_stack:
            self.fwd_stack.append(self.curr)
            self.curr = self.back_stack.pop()
            steps -= 1
        return self.curr

    def forward(self, steps):
        while steps > 0 and self.fwd_stack:
            self.back_stack.append(self.curr)
            self.curr = self.fwd_stack.pop()
            steps -= 1
        return self.curr


# Part B: Stack using two queues

class Queue:
    def __init__(self):
        self.q = []

    def enqueue(self, val):
        self.q.append(val)

    def dequeue(self):
        if not self.empty():
            return self.q.pop(0)
        return None

    def peek(self):
        if not self.empty():
            return self.q[0]
        return None

    def empty(self):
        return len(self.q) == 0


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):
        self.q2.enqueue(x)
        while not self.q1.empty():
            self.q2.enqueue(self.q1.dequeue())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.empty():
            return None
        return self.q1.dequeue()

    def top(self):
        if self.empty():
            return None
        return self.q1.peek()

    def empty(self):
        return self.q1.empty()
