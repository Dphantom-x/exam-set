# SET 2430 - Week 6 In-Class Code & Practice (Oct 7)
# Topics: Singly Linked List, Doubly Linked List, Dynamic Array Append Timing, Binary Tree Intro

import time

# ==========================================
# 1. Array Append Benchmark (Amortized O(1))
# ==========================================
def run_append_benchmarks():
    print("--- Dynamic Array Resizing Benchmarks ---")
    
    # Test 1: 1,000,000 appends
    my_list = []
    start_time = time.time()
    for i in range(1000000):
        my_list.append(i)
    end_time = time.time()
    print(f"1,000,000 appends took: {end_time - start_time:.4f} seconds (~0.05-0.10s)")

    # Test 2: 10,000,000 appends
    my_list = []
    start_time = time.time()
    for i in range(10000000):
        my_list.append(i)
    end_time = time.time()
    print(f"10,000,000 appends took: {end_time - start_time:.4f} seconds (scaled linearly!)")


# ==========================================
# 2. Singly Linked List (Oct 7 Practice)
# ==========================================
# OCT 7 Practice Question: Create a Singly Linked List
# A Node should store:
#   - a value (data)
#   - a reference to the next node (next)
# SinglyLinkedList should keep track of head and size.

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, val):
        """Append to tail: O(n) without tail pointer, or O(1) with tail."""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    def addAtHead(self, val):
        """Insert at beginning: O(1)"""
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val):
        """Insert at end: O(n)"""
        self.append(val)

    def get(self, index):
        """Get value at index: O(n)"""
        if index < 0 or index >= self.size:
            return -1
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def deleteAtIndex(self, index):
        """Delete node at index: O(n)"""
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next
        self.size -= 1

    def display(self):
        vals = []
        curr = self.head
        while curr:
            vals.append(str(curr.data))
            curr = curr.next
        return " -> ".join(vals) + " -> None"


# ==========================================
# 3. Doubly Linked List Structure
# ==========================================
class DoublyNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, val):
        new_node = DoublyNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1


# ==========================================
# 4. Binary Tree Node & Recurrence Intro
# ==========================================
# T(n) = 2T(n/2) + c  => O(n) for tree traversal
class TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def count_tree_nodes(root):
    if root is None:
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)


if __name__ == '__main__':
    run_append_benchmarks()

    print("\n--- Singly Linked List Test ---")
    sll = SinglyLinkedList()
    sll.addAtHead(10)
    sll.append(20)
    sll.append(30)
    sll.addAtHead(5)
    print("List contents:", sll.display())
    print("Size:", sll.size)
    print("Item at index 2:", sll.get(2))
    sll.deleteAtIndex(1)
    print("After deleting index 1:", sll.display())

    print("\n--- Binary Tree Node Test ---")
    node1 = TreeNode(100)
    node1.left = TreeNode(101)
    node1.right = TreeNode(102)
    node1.left.left = TreeNode(103)
    print("Total nodes:", count_tree_nodes(node1))
