# SET 2430 — Week 7: Circular & Doubly Linked Lists, Stacks, and Queues

Prof. Haiying Xiao · Fall 2026

---

## 1. Circular Linked Lists

A **Circular Linked List** is a sequence of elements where each node references the next node, and the **last node references back to the `head` node** rather than pointing to `None`/`NULL`.

```
head
 ↓
[Val: 100 | right] ──> [Val: 200 | right] ──> [Val: 300 | right]
        ↑                                              │
        └──────────────────────────────────────────────┘
```

### In-Class Implementation (Prof. Xiao Convention)
In her code notes, Prof. Xiao uses `right` as the forward pointer for node links:

```python
class Node:
    def __init__(self, val):
        self.value = val
        self.right = None  # Pointer to next node


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            new_node.right = new_node  # Points to itself
            return

        # Find the last node (whose right pointer points to head)
        curr = self.head
        while curr.right != self.head:
            curr = curr.right

        new_node.right = self.head
        curr.right = new_node
        self.head = new_node

    def print_list(self):
        if not self.head:
            print("Empty List")
            return
        curr = self.head
        vals = []
        while True:
            vals.append(str(curr.value))
            curr = curr.right
            if curr == self.head:
                break
        print(" -> ".join(vals) + " -> (back to head)")
```

### Real-World Applications
1. **Round-Robin Scheduling**: Operating systems CPU process time slices.
2. **Multiplayer Turn-Based Games**: Cycling player turns in a ring.
3. **Media Playlists**: Continuous looping of songs.

---

## 2. Doubly Linked Lists

A **Doubly Linked List** allows traversal in both forward and backward directions. Each node contains:
* `value` (or `data`)
* `left` (or `prev`): Pointer to previous node
* `right` (or `next`): Pointer to next node

```
None <── [left | 100 | right] <══=> [left | 200 | right] <══=> [left | 300 | right] ──> None
```

### In-Class Implementation

```python
class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.left = None   # prev
        self.right = None  # next


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        """Append to tail: O(1)"""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
        self.size += 1

    def addAtHead(self, value):
        """Insert at head: O(1)"""
        new_node = DoublyNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
        self.size += 1

    def get(self, index):
        """Get value at index: O(n)"""
        if index < 0 or index >= self.size:
            return None
        # Optimize traversal: start from head if index in first half, else from tail
        if index < self.size // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.right
        else:
            curr = self.tail
            for _ in range(self.size - 1 - index):
                curr = curr.left
        return curr.value

    def countNodes(self):
        return self.size

    def print_forward(self):
        curr = self.head
        vals = []
        while curr:
            vals.append(str(curr.value))
            curr = curr.right
        print(" <-> ".join(vals))
```

---

## 3. Stacks (LIFO) & Queues (FIFO)

### A. Stack (Last In, First Out)
* Elements are added and removed from the **same end (Top)**.
* Analogy: Stack of cafeteria trays / undo history.
* **Core Methods**:
  * `push(x)`: $O(1)$
  * `pop()`: $O(1)$
  * `top()` / `peek()`: $O(1)$
  * `empty()`: $O(1)$

### B. Queue (First In, First Out)
* Elements are added at the **Rear** and removed from the **Front**.
* Analogy: Line at a ticket counter.
* **Core Methods**:
  * `enqueue(x)`: $O(1)$
  * `dequeue()`: $O(1)$
  * `front()`: $O(1)$
  * `empty()`: $O(1)$

---

## 4. Assignment 5 Overview & Concepts

Assignment 5 covers practical applications of these linear data structures:

### Part A: Browser History Navigation
* **Problem**: Emulate browser back/forward buttons with a starting homepage.
  * `visit(url)`: Visits new URL and discards all forward history.
  * `back(steps)`: Goes back up to `steps` in history.
  * `forward(steps)`: Moves forward up to `steps` in history.
* **Algorithmic approaches**:
  1. **Two Stacks**: `back_stack` and `forward_stack`.
  2. **Doubly Linked List**: Nodes store URLs; back/forward traverse `left`/`right`.
  3. **Dynamic Array + Pointer Index**: Fast $O(1)$ arithmetic navigation.

### Part B: LIFO Stack Using Two FIFO Queues
* **Problem**: Build a LIFO stack where internal storage can only use queue operations (`enqueue` / `dequeue`).
* **Approach**:
  * On `push(x)`: Enqueue $x$ into `q2`, transfer all elements from `q1` to `q2`, then swap `q1` and `q2`.
  * `q1`'s front always contains the top of the stack!
  * `pop()` and `top()` become $O(1)$ directly from `q1`.
