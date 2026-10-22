"""
SET 2430: Algorithmic Design and Data Structures
Master Code Library: All 10 Linear Data Structures
Prof. Haiying Xiao · Fall 2026

Complete, verified Python implementations with full edge-case handling:
1. Singly Linked List
2. Doubly Linked List
3. Circular Singly Linked List
4. Circular Doubly Linked List
5. Stack (Array-Based)
6. Stack (Linked-List-Based)
7. Queue (Array-Based Circular Buffer)
8. Queue (Linked-List-Based)
9. Deque (Array-Based Circular Buffer)
10. Deque (Doubly-Linked-List-Based)
"""

# =====================================================================
# 1. SINGLY LINKED LIST
# =====================================================================
class SinglyNode:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        """Insert at index 0: O(1)"""
        new_node = SinglyNode(val, self.head)
        self.head = new_node
        self.size += 1

    def append(self, val):
        """Insert at tail: O(n) without tail pointer"""
        new_node = SinglyNode(val)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def get(self, index):
        """Access element by index: O(n)"""
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def deleteAtIndex(self, index):
        """Delete node at index: O(n)"""
        if index < 0 or index >= self.size:
            return False
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1
        return True

    def reverse(self):
        """In-place reversal: O(n) time, O(1) space"""
        prev = None
        curr = self.head
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        self.head = prev

    def display(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return " -> ".join(res) + " -> None"


# =====================================================================
# 2. DOUBLY LINKED LIST
# =====================================================================
class DoublyNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev   # Also called self.left in Xiao's notes
        self.next = next   # Also called self.right in Xiao's notes


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtHead(self, val):
        """Insert at head: O(1)"""
        new_node = DoublyNode(val, None, self.head)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def append(self, val):
        """Insert at tail: O(1) using tail pointer"""
        new_node = DoublyNode(val, self.tail, None)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def delete(self, target):
        """Delete first occurrence of target: O(n)"""
        curr = self.head
        while curr:
            if curr.data == target:
                if curr == self.head and curr == self.tail: # Only 1 node
                    self.head = self.tail = None
                elif curr == self.head:                     # Delete head
                    self.head = self.head.next
                    self.head.prev = None
                elif curr == self.tail:                     # Delete tail
                    self.tail = self.tail.prev
                    self.tail.next = None
                else:                                       # Middle node
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                self.size -= 1
                return True
            curr = curr.next
        return False

    def display_forward(self):
        res = []
        curr = self.head
        while curr:
            res.append(str(curr.data))
            curr = curr.next
        return " <-> ".join(res) if res else "Empty"

    def display_backward(self):
        res = []
        curr = self.tail
        while curr:
            res.append(str(curr.data))
            curr = curr.prev
        return " <-> ".join(res) if res else "Empty"


# =====================================================================
# 3. CIRCULAR SINGLY LINKED LIST
# =====================================================================
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        """Insert at head: O(n) without tail pointer, or O(1) with tail"""
        new_node = SinglyNode(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            new_node.next = self.head
            curr.next = new_node
            self.head = new_node
        self.size += 1

    def append(self, val):
        """Insert at tail: O(n)"""
        new_node = SinglyNode(val)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head
        self.size += 1

    def deleteHead(self):
        """Delete head node: O(n) without tail pointer"""
        if not self.head:
            return False
        if self.head.next == self.head: # 1 node
            self.head = None
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = self.head.next
            self.head = self.head.next
        self.size -= 1
        return True

    def display(self):
        if not self.head:
            return "Empty"
        res = []
        curr = self.head
        while True:
            res.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        return " -> ".join(res) + " -> (head: " + str(self.head.data) + ")"


# =====================================================================
# 4. CIRCULAR DOUBLY LINKED LIST
# =====================================================================
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        """Insert at head: O(1) instantaneous!"""
        new_node = DoublyNode(val)
        if not self.head:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node
        self.size += 1

    def append(self, val):
        """Insert at tail: O(1) (tail is just self.head.prev)"""
        self.addAtHead(val)
        self.head = self.head.next # Shift head forward so new node is tail

    def delete(self, target):
        """Delete target: O(n) search, O(1) unlinking"""
        if not self.head:
            return False
        curr = self.head
        while True:
            if curr.data == target:
                if curr.next == curr: # Only 1 node
                    self.head = None
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    if curr == self.head:
                        self.head = curr.next
                self.size -= 1
                return True
            curr = curr.next
            if curr == self.head:
                break
        return False

    def display(self):
        if not self.head:
            return "Empty"
        res = []
        curr = self.head
        while True:
            res.append(str(curr.data))
            curr = curr.next
            if curr == self.head:
                break
        return " <-> ".join(res) + " <-> (head: " + str(self.head.data) + ")"


# =====================================================================
# 5. STACK (ARRAY-BASED)
# =====================================================================
class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        """Add to top: O(1) amortized"""
        self.stack.append(val)

    def pop(self):
        """Remove and return top: O(1)"""
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        """Return top without removing: O(1)"""
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


# =====================================================================
# 6. STACK (LINKED-LIST-BASED)
# =====================================================================
class LinkedStack:
    def __init__(self):
        self.head = None  # Head is the TOP of the stack
        self._size = 0

    def push(self, val):
        """Add to top: O(1) strictly (no reallocation ever)"""
        new_node = SinglyNode(val, self.head)
        self.head = new_node
        self._size += 1

    def pop(self):
        """Remove and return top: O(1)"""
        if self.is_empty():
            return None
        popped_val = self.head.data
        self.head = self.head.next
        self._size -= 1
        return popped_val

    def peek(self):
        """Inspect top: O(1)"""
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size


# =====================================================================
# 7. QUEUE (ARRAY-BASED CIRCULAR BUFFER)
# =====================================================================
class ArrayQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, val):
        """Add to rear: O(1)"""
        if self.is_full():
            raise OverflowError("Queue is full")
        self.arr[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def dequeue(self):
        """Remove from front: O(1) (NO array shifting!)"""
        if self.is_empty():
            return None
        val = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

    def peek(self):
        """Inspect front: O(1)"""
        if self.is_empty():
            return None
        return self.arr[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count


# =====================================================================
# 8. QUEUE (LINKED-LIST-BASED)
# =====================================================================
class LinkedQueue:
    def __init__(self):
        self.head = None  # Front of queue (dequeue from here)
        self.tail = None  # Rear of queue (enqueue here)
        self._size = 0

    def enqueue(self, val):
        """Add to rear: O(1)"""
        new_node = SinglyNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove from front: O(1)"""
        if self.is_empty():
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:  # Queue became empty
            self.tail = None
        self._size -= 1
        return val

    def peek(self):
        """Inspect front: O(1)"""
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.head is None

    def size(self):
        return self._size


# =====================================================================
# 9. DEQUE (ARRAY-BASED CIRCULAR BUFFER)
# =====================================================================
class ArrayDeque:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.arr = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    def append(self, val):
        """Add to right (rear): O(1)"""
        if self.is_full():
            raise OverflowError("Deque is full")
        self.arr[self.rear] = val
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    def appendleft(self, val):
        """Add to left (front): O(1)"""
        if self.is_full():
            raise OverflowError("Deque is full")
        # Step front backwards with wrap-around
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.arr[self.front] = val
        self.count += 1

    def pop(self):
        """Remove from right (rear): O(1)"""
        if self.is_empty():
            return None
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        val = self.arr[self.rear]
        self.arr[self.rear] = None
        self.count -= 1
        return val

    def popleft(self):
        """Remove from left (front): O(1)"""
        if self.is_empty():
            return None
        val = self.arr[self.front]
        self.arr[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return val

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def size(self):
        return self.count


# =====================================================================
# 10. DEQUE (LINKED-LIST-BASED)
# =====================================================================
class LinkedDeque:
    def __init__(self):
        self.head = None  # Front
        self.tail = None  # Rear
        self._size = 0

    def append(self, val):
        """Add to right (rear): O(1)"""
        new_node = DoublyNode(val, prev=self.tail, next=None)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def appendleft(self, val):
        """Add to left (front): O(1)"""
        new_node = DoublyNode(val, prev=None, next=self.head)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def pop(self):
        """Remove from right (rear): O(1)"""
        if self.is_empty():
            return None
        val = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self._size -= 1
        return val

    def popleft(self):
        """Remove from left (front): O(1)"""
        if self.is_empty():
            return None
        val = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self._size -= 1
        return val

    def peek(self):
        return self.tail.data if self.tail else None

    def peekleft(self):
        return self.head.data if self.head else None

    def is_empty(self):
        return self._size == 0

    def size(self):
        return self._size


# =====================================================================
# COMPREHENSIVE VERIFICATION TESTS
# =====================================================================
if __name__ == '__main__':
    print("Testing 1. SinglyLinkedList...")
    sll = SinglyLinkedList()
    sll.addAtHead(10); sll.append(20); sll.append(30); sll.addAtHead(5)
    assert sll.display() == "5 -> 10 -> 20 -> 30 -> None"
    sll.reverse()
    assert sll.display() == "30 -> 20 -> 10 -> 5 -> None"

    print("Testing 2. DoublyLinkedList...")
    dll = DoublyLinkedList()
    dll.addAtHead(10); dll.append(20); dll.append(30)
    assert dll.display_forward() == "10 <-> 20 <-> 30"
    assert dll.display_backward() == "30 <-> 20 <-> 10"

    print("Testing 3. CircularSinglyLinkedList...")
    csll = CircularSinglyLinkedList()
    csll.addAtHead(10); csll.append(20); csll.addAtHead(5)
    assert csll.display() == "5 -> 10 -> 20 -> (head: 5)"

    print("Testing 4. CircularDoublyLinkedList...")
    cdll = CircularDoublyLinkedList()
    cdll.addAtHead(10); cdll.append(20); cdll.addAtHead(5)
    assert cdll.display() == "5 <-> 10 <-> 20 <-> (head: 5)"

    print("Testing 5. ArrayStack & 6. LinkedStack...")
    for S in [ArrayStack(), LinkedStack()]:
        S.push(10); S.push(20)
        assert S.peek() == 20
        assert S.pop() == 20
        assert S.pop() == 10
        assert S.is_empty()

    print("Testing 7. ArrayQueue & 8. LinkedQueue...")
    for Q in [ArrayQueue(5), LinkedQueue()]:
        Q.enqueue(100); Q.enqueue(200)
        assert Q.peek() == 100
        assert Q.dequeue() == 100
        assert Q.dequeue() == 200
        assert Q.is_empty()

    print("Testing 9. ArrayDeque & 10. LinkedDeque...")
    for D in [ArrayDeque(5), LinkedDeque()]:
        D.append(20); D.appendleft(10); D.append(30)
        assert D.popleft() == 10
        assert D.pop() == 30
        assert D.pop() == 20
        assert D.is_empty()

    print("\nALL 10 DATA STRUCTURES PASSED WITH 100% INTEGRITY!")
