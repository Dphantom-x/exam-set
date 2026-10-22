# SET 2430: Paper-Based Coding & No-IDE Exam Survival Master Guide
**Course:** SET 2430 — Algorithmic Design and Data Structures  
**Instructor:** Prof. Haiying Xiao | New York City College of Technology (CUNY)  
**Target:** In-Person Paper Midterms, Finals, and Pop-Quizzes (Python 3)

---

## Table of Contents
1. [The Psychology & Reality of Paper CS Exams](#1-the-psychology--reality-of-paper-cs-exams)
2. [Defensive Handwritten Python Formatting Standards](#2-defensive-handwritten-python-formatting-standards)
3. [Mastering the "Trace Table" Technique for Code Output Questions](#3-mastering-the-trace-table-technique-for-code-output-questions)
4. [Pointer Diagramming Rules (The Box-and-Pointer Protocol)](#4-pointer-diagramming-rules-the-box-and-pointer-protocol)
5. [The 7 Universal Edge Cases for Every Data Structure on Paper](#5-the-7-universal-edge-cases-for-every-data-structure-on-paper)
6. [Handwritten "Cheat Sheet" Templates (Prof. Xiao Convention)](#6-handwritten-cheat-sheet-templates-prof-xiao-convention)
7. [Recurrence Relations Expansion Proof Protocol](#7-recurrence-relations-expansion-proof-protocol)
8. [The 10-Minute Pre-Submission Paper Exam Audit Checklist](#8-the-10-minute-pre-submission-paper-exam-audit-checklist)

---

# 1. The Psychology & Reality of Paper CS Exams

Writing Python code on paper without an Integrated Development Environment (IDE) is a fundamentally different cognitive challenge than coding in VS Code, PyCharm, or Jupyter Notebooks. On a computer, the machine provides an immediate safety net. On paper, **you are the compiler, the CPU, the memory manager, and the test suite.**

```
┌───────────────────────────────────────┬────────────────────────────────────────┐
│ IDE Coding (Safety Net Present)       │ Paper Coding (Zero External Safety)    │
├───────────────────────────────────────┼────────────────────────────────────────┤
│ Syntax errors underlined in red wavy lines │ Invisible syntax errors cost full marks│
│ Auto-indentation on Enter             │ Ambiguous tabs/spaces ruin block scope │
│ Backspace & Ctrl+Z are instantaneous  │ Erasing wastes 20-30% of exam clock    │
│ `print()` debugging and REPL probing  │ Static mental execution required       │
│ Auto-complete / IntelliSense methods  │ Exact method/field names must be memorized│
└───────────────────────────────────────┴────────────────────────────────────────┘
```

### The 4 Major Failure Modes on Paper Exams
1. **The "Start Writing Immediately" Trap**: Students begin inking line 1 of code before sketching pointer mutations. Within 4 lines, they realize they orphaned a node, erase furiously, smudge the page, and run out of vertical margin space.
2. **The "Vanishing Scope" Indentation Drift**: As handwriting shifts diagonally across unlined paper, an `if` block's indentation drifts leftward until it aligns with the outer loop, changing algorithm logic.
3. **The "Colons & Self" Tax**: Prof. Xiao and DSA graders deduct 0.5 to 1 point per omitted colon, forgotten `self.` attribute prefix, or missing `self` formal parameter. Accumulating 6 of these drops an "A" answer to a "C+".
4. **The "Dangling Reference" Crash**: Rewiring `curr.right = new_node` before pointing `new_node.right = curr.right`, forever severing access to the rest of the linked chain.

---

# 2. Defensive Handwritten Python Formatting Standards

Handwritten Python requires deliberate, defensive visual structure so that the grading professor can never misinterpret your block scopes or deduct points for ambiguity.

```
Defensive Indentation Box Rule:
================================
def addAtHead(self, val):                <-- Colon mandatory!
|   new_node = DoublyNode(val)           <-- 1 Guide line (|) = 1 indent level
|   if self.head is None:                <-- Colon mandatory!
|   |   self.head = new_node             <-- 2 Guide lines (||) = nested block
|   |   self.tail = new_node
|   else:                                <-- Aligned with matching `if`
|   |   new_node.right = self.head
|   |   self.head.left = new_node
|   |   self.head = new_node
|   self.size += 1                       <-- Snapped back to function body level!
```

### A. The Vertical Guideline Rule (The "Ruler Trick")
- When writing on blank or lined test paper, lightly draw a faint vertical pencil line (or mark small tick marks) where your indentation column begins.
- Use **2 to 3 standard character widths** per indent level. Do NOT use microscopic 1-space shifts.
- When an indentation block terminates (e.g. exiting an `if` or `while`), ensure the next line strictly snaps back to align with the parent keyword.

### B. The "Colons & Self" Pre-Flight Checklist
Before moving to the next question, spend 10 seconds performing this exact scan:

1. **Header Colons**: Check every `def`, `class`, `if`, `elif`, `else`, `while`, `for`, `try`, `except`. Does every line end with `:`?
2. **Method Formal Parameters**: Check every method inside a class. Is `self` the very first parameter? (`def __init__(self, val):`, `def append(self, val):`).
3. **Instance Attributes**: Check every reference to instance state. Did you write `head` or `self.head`? Did you write `size` or `self.size`?
   > **Fatal Hand-Written Error**: Writing `head = new_node` instead of `self.head = new_node` creates an ephemeral local variable that vanishes upon function return. The list remains unmodified!
4. **Equality vs. Assignment**: Check conditional statements. Did you write `if curr.right = self.head:` (syntax error) instead of `if curr.right == self.head:`?

### C. Scratch Paper Strategic Partitioning
Never write final code directly into the exam answer box. Divide your scratch paper into three distinct visual quadrants:

```
┌───────────────────────────────────────┬────────────────────────────────────────┐
│ ZONE 1: Box-and-Pointer Diagram       │ ZONE 3: Clean Draft Code               │
│                                       │                                        │
│  [Head] -> [A] <==> [B] -> None       │  def delete(self, key):                │
│             ^                         │      curr = self.head                  │
│            curr                       │      while curr and curr.value != key: │
│                                       │          curr = curr.right             │
├───────────────────────────────────────┤      if not curr:                      │
│ ZONE 2: Edge Cases & Trace Table      │          return False                  │
│                                       │      # Rewire pointers...              │
│  [X] Empty list (head is None)        │                                        │
│  [X] 1-element list                   │                                        │
│  [X] Delete head node                 │                                        │
│  [X] Delete tail node                 │                                        │
└───────────────────────────────────────┴────────────────────────────────────────┘
```
1. **Zone 1 (Top-Left)**: Box-and-pointer diagram of the initial state, new nodes, and arrow transitions.
2. **Zone 2 (Bottom-Left)**: Edge-case checklist and trace variable table.
3. **Zone 3 (Right Side)**: Rapid pencil draft of the code. Once verified against Zone 1 & 2, copy it cleanly into the exam booklet.

---

# 3. Mastering the "Trace Table" Technique for Code Output Questions

Prof. Xiao frequently provides 10-15 lines of linked list or recursive code and asks: *"What is the output?"* or *"What is the state of the list after execution?"*

Guessing in your head causes 80% of lost points on paper exams. Use the **Standardized Paper Trace Table**.

### A. Standardized Trace Table Grid
When tracing loops and pointer re-assignments, draw this 5-column table on scratch paper:

| Step / Line # | Condition Evaluated | Variables (`curr`, `prev`) | Pointer Link / Value State | Output / Action Taken |
| :---: | :---: | :---: | :---: | :---: |
| Init | — | `curr = head (Node 10)` | `10 -> 20 -> 30 -> head` | Start circular traversal |
| L4 | `curr.right != head` (20 != 10) -> **True** | `curr = Node 20` | `curr` moved to next | None |
| L4 | `curr.right != head` (30 != 10) -> **True** | `curr = Node 30` | `curr` moved to tail | None |
| L4 | `curr.right != head` (10 != 10) -> **False** | `curr = Node 30` | Loop terminates | Tail node found: Node 30 |
| L7 | — | `new_node (Node 5)` | `new_node.right = head` | `5 -> 10` |
| L8 | — | `curr (Node 30)` | `curr.right = new_node` | `30 -> 5` |
| L9 | — | `self.head` | `self.head = new_node` | Head pointer updated to 5 |

### B. The Recursive Call Stack Diagram (Box Frame Method)
For recursive functions (Factorial, Tree Traversals, Divide-and-Conquer), draw call frames as a stack growing **upwards**:

```
Tracing: count_tree_nodes(root) on tree:      (10)
                                             /    \
                                           (5)    (15)

Call Stack Trace (Push upward, Resolve downward):

▲ [Frame 5: count_tree_nodes(None)] -> Returns 0
│ [Frame 4: count_tree_nodes(None)] -> Returns 0
│ [Frame 3: count_tree_nodes(Node 5)]
│    root.val = 5
│    left_res = Frame 4 (0)
│    right_res = Frame 5 (0)
│    return 1 + 0 + 0 = 1 ────────────────────────┐ (Bubbles return down)
│                                                  │
│ [Frame 2: count_tree_nodes(Node 15)]             ▼
│    root.val = 15                               [Returns 1]
│    return 1 + 0 + 0 = 1 ─────────┐               │
│                                  ▼               │
│ [Frame 1: count_tree_nodes(Node 10)]             │
│    root.val = 10                                 │
│    left_res = 1 <────────────────────────────────┘
│    right_res = 1 <───────────────┘
│    return 1 + 1 + 1 = 3 (FINAL OUTPUT)
└───────────────────────────────────────────────────
```

#### The 4 Rules for Paper Recursion Tracing:
1. Every recursive call gets its own distinct box with its own local parameter values.
2. Label each box with its **Calling Line** and **Waiting State** (e.g. `Waiting for right child`).
3. When reaching the Base Case (`root is None`), write `RETURN <val>` and draw an arrow pointing down into the waiting parent frame.
4. Substitute the returned value directly into the parent expression before calculating the parent's return.

---

# 4. Pointer Diagramming Rules (The Box-and-Pointer Protocol)

The single greatest source of runtime crashes in linked list code is **memory dereferencing order errors** (e.g., `AttributeError: 'NoneType' object has no attribute 'right'`).

### The Golden Rule of Pointer Mutation
> **NEVER break an existing reference arrow until the new node is anchored into the chain!**  
> Anchor the new node's outgoing pointers first; rewire existing pointers second; update `head`/`tail` last.

```
       Step 1: Current State
       self.head
           │
           ▼
       ┌───────┬───────┐      ┌───────┬───────┐
       │   A   │ right ├─────►│   B   │ None  │
       └───────┴───────┘      └───────┴───────┘

       Step 2 & 3: Floating Node & Anchor New Outgoing Pointer FIRST!
       self.head
           │
           ▼
       ┌───────┬───────┐      ┌───────┬───────┐
       │   A   │ right ├─────►│   B   │ None  │
       └───────┴───────┘      └───────┴───────┘
               ▲
               │ (3. new_node.right = self.head) [DASHED = NEW]
       ┌───────┴───────┐
       │  NEW  │ right │
       └───────┬───────┘
           ▲
           │
        new_node

       Step 4 & 5: Update Head Pointer
       self.head ─────────────┐
                              ▼
       ┌───────┬───────┐      ┌───────┬───────┐
       │  NEW  │ right ├─────►│   A   │ right ├─────► ...
       └───────┴───────┘      └───────┴───────┘
```

### The 5-Step Box-and-Pointer Protocol:
1. **Step 1: Draw Current Nodes**: Draw every existing node as a box split into data and pointer fields. Label `self.head` and `self.tail`.
2. **Step 2: Draw the New Node in Isolation**: Draw `new_node` floating separately above or below the chain.
3. **Step 3: Connect Outgoing Links First (Dashed Arrows)**:
   - For Singly Linked `addAtHead`: `new_node.next = self.head`
   - For Doubly Linked `append`: `new_node.left = self.tail`
   - For Circular `addAtHead`: `new_node.right = self.head`
4. **Step 4: Cross Out Old Broken Arrows (X Marks)**:
   - Put an explicit `X` over the pointer arrow that is being rewritten.
   - For Doubly Linked `append`: `self.tail.right = new_node`
5. **Step 5: Advance Structure Pointers**:
   - Update `self.head = new_node` or `self.tail = new_node`.
   - Update counter: `self.size += 1`.

---

# 5. The 7 Universal Edge Cases for Every Data Structure on Paper

Before writing the core logic of any data structure operation on paper, check off the **Universal 7 Edge Cases**. Prof. Xiao's grading rubrics dedicate 30-40% of points purely to defensive edge handling.

```
┌────┬─────────────────────────────┬─────────────────────────────────────────────────┐
│ #  │ Edge Case Condition         │ Defensive Python Code Snippet                   │
├────┼─────────────────────────────┼─────────────────────────────────────────────────┤
│ 1  │ Empty Structure             │ if self.head is None: (or if self.size == 0:)   │
│ 2  │ Single-Node Structure       │ if self.head.right is None: (or curr.right == h)│
│ 3  │ Operation at Index 0 (Head) │ if index == 0: self.addAtHead(val); return      │
│ 4  │ Operation at Tail (size - 1)│ if index == self.size - 1: self.append(val)     │
│ 5  │ Index Out of Bounds         │ if index < 0 or index >= self.size: return None │
│ 6  │ Target Element Not Found    │ while curr and curr.value != target: ...        │
│ 7  │ Size Counter Synchronization│ self.size += 1 (insert) / self.size -= 1 (del)  │
└────┴─────────────────────────────┴─────────────────────────────────────────────────┘
```

### Deep Dive into the 7 Edge Cases:

#### 1. Empty Structure (`self.head is None`)
- **Insertion**: The new node becomes both `self.head` and `self.tail`. If circular, its next pointer must point to itself!
- **Deletion / Search**: Cannot delete or search an empty structure; immediately `return None` or `return False`.

#### 2. Single-Node Structure
- **Doubly Linked List**: `self.head == self.tail`. Deleting this node requires setting BOTH `self.head = None` and `self.tail = None`.
- **Circular Linked List**: `self.head.right == self.head`. Deleting this node requires setting `self.head = None`.

#### 3. Operation at Index 0 (Head Operation)
- Deleting the head node:
  ```python
  self.head = self.head.right
  if self.head:               # If list is not now empty
      self.head.left = None   # Sever backward pointer in Doubly list
  else:
      self.tail = None        # List became empty
  ```

#### 4. Operation at Tail (`index == self.size - 1`)
- Inserting at tail with a `tail` pointer is $O(1)$:
  ```python
  self.tail.right = new_node
  new_node.left = self.tail
  self.tail = new_node
  ```
- Deleting at tail:
  ```python
  self.tail = self.tail.left
  if self.tail:
      self.tail.right = None
  else:
      self.head = None
  ```

#### 5. Index Out of Bounds
- Always check bounds before traversing:
  ```python
  if index < 0 or index >= self.size:
      return None  # Or raise IndexError("Out of bounds")
  ```

#### 6. Target Search Failure
- When traversing by value, always check for null pointer termination:
  ```python
  curr = self.head
  while curr is not None and curr.value != target:
      curr = curr.right
  if curr is None:
      return -1  # Target not found in list
  ```

#### 7. Size Variable Synchronization
- Forgetting to increment or decrement `self.size` silently breaks all subsequent bound checks and `len()` calls:
  - On insert: `self.size += 1`
  - On successful delete: `self.size -= 1`

---

# 6. Handwritten "Cheat Sheet" Templates (Prof. Xiao Convention)

> **Naming Note for Prof. Xiao's Exams**:  
> In lecture, Prof. Xiao frequently uses:
> - `right` for the forward pointer (`next`)
> - `left` for the backward pointer (`prev`)
> - `value` or `data` for node contents  
> *Both `next`/`prev` and `right`/`left` are standard; using Prof. Xiao's `left`/`right` convention demonstrates direct lecture alignment.*

---

### A. Node Definitions

```python
# 1. Singly Linked Node
class Node:
    def __init__(self, val):
        self.value = val
        self.right = None  # Or self.next


# 2. Doubly Linked Node (Prof. Xiao Convention)
class DoublyNode:
    def __init__(self, val):
        self.value = val
        self.left = None   # Previous pointer (prev)
        self.right = None  # Next pointer (next)


# 3. Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.value = val
        self.left = None   # Left child
        self.right = None  # Right child
```

---

### B. Singly Linked List (Complete Paper Template)

```python
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addAtHead(self, val):
        """O(1) insertion at head"""
        new_node = Node(val)
        new_node.right = self.head
        self.head = new_node
        self.size += 1

    def append(self, val):
        """O(n) insertion at tail without tail pointer"""
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.right is not None:
                curr = curr.right
            curr.right = new_node
        self.size += 1

    def get(self, index):
        """O(n) indexed lookup"""
        if index < 0 or index >= self.size:
            return None
        curr = self.head
        for _ in range(index):
            curr = curr.right
        return curr.value

    def deleteAtIndex(self, index):
        """O(n) deletion at index with predecessor tracking"""
        if index < 0 or index >= self.size:
            return None

        # Edge Case: Delete Head
        if index == 0:
            deleted_val = self.head.value
            self.head = self.head.right
            self.size -= 1
            return deleted_val

        curr = self.head
        for _ in range(index - 1):
            curr = curr.right

        deleted_val = curr.right.value
        curr.right = curr.right.right
        self.size -= 1
        return deleted_val

    def find(self, target):
        """O(n) linear search"""
        curr = self.head
        index = 0
        while curr is not None:
            if curr.value == target:
                return index
            curr = curr.right
            index += 1
        return -1
```

---

### C. Doubly Linked List (Prof. Xiao Convention with `left`/`right`)

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addAtHead(self, val):
        """O(1) insert at head"""
        new_node = DoublyNode(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.right = self.head
            self.head.left = new_node
            self.head = new_node
        self.size += 1

    def append(self, val):
        """O(1) insert at tail using tail pointer"""
        new_node = DoublyNode(val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
        self.size += 1

    def delete(self, target_val):
        """O(n) search + O(1) pointer rewire for arbitrary node"""
        if self.head is None:
            return False

        curr = self.head
        while curr is not None and curr.value != target_val:
            curr = curr.right

        if curr is None:
            return False  # Target not found

        # Case 1: Target is Head
        if curr == self.head:
            self.head = self.head.right
            if self.head:
                self.head.left = None
            else:
                self.tail = None  # List is now empty
        # Case 2: Target is Tail
        elif curr == self.tail:
            self.tail = self.tail.left
            self.tail.right = None
        # Case 3: Target is in Middle
        else:
            curr.left.right = curr.right
            curr.right.left = curr.left

        self.size -= 1
        return True
```

---

### D. Circular Linked List (Prof. Xiao Lecture Code)

```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val):
        """Insert at head and maintain loop: O(n) without tail pointer"""
        new_node = Node(val)

        # Edge Case: Empty list
        if not self.head:
            self.head = new_node
            new_node.right = new_node  # Points to itself!
            return

        # Find the last node (whose right pointer points back to head)
        curr = self.head
        while curr.right != self.head:  # THE ESSENTIAL CIRCULAR LOOP CONDITION
            curr = curr.right

        # Rewire pointers
        new_node.right = self.head
        curr.right = new_node
        self.head = new_node

    def print_list(self):
        """Defensive traversal that avoids infinite loops"""
        if not self.head:
            print("Empty")
            return

        curr = self.head
        elements = []
        while True:
            elements.append(str(curr.value))
            curr = curr.right
            if curr == self.head:
                break
        print(" -> ".join(elements) + " -> (head)")
```

---

### E. Stack ADT (LIFO: Last In, First Out)

```python
# Array-backed Stack implementation
class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        """O(1) amortized"""
        self.items.append(val)

    def pop(self):
        """O(1) pop from top"""
        if self.empty():
            return None
        return self.items.pop()

    def peek(self):
        """O(1) inspect top"""
        if self.empty():
            return None
        return self.items[-1]

    def empty(self):
        """O(1) check"""
        return len(self.items) == 0

    def size(self):
        return len(self.items)
```

---

### F. Queue ADT (FIFO: First In, First Out)

```python
# Standard Queue ADT (Prof. Xiao Assignment 5 Convention)
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        """O(1) amortized enqueue at rear"""
        self.items.append(val)

    def dequeue(self):
        """O(n) with Python list pop(0), or O(1) with collections.deque"""
        if self.empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """O(1) front inspection"""
        if self.empty():
            return None
        return self.items[0]

    def empty(self):
        """O(1) check"""
        return len(self.items) == 0
```

---

### G. Classic Recursion Paper Templates

```python
# 1. Factorial: T(n) = T(n-1) + O(1) => O(n) Time, O(n) Auxiliary Stack Space
def factorial(n):
    if n <= 1:  # Base Case
        return 1
    return n * factorial(n - 1)  # Recursive Step


# 2. Binary Tree Node Counter: T(n) = 2T(n/2) + O(1) => O(n) Time
def count_tree_nodes(root):
    if root is None:  # Base Case
        return 0
    return 1 + count_tree_nodes(root.left) + count_tree_nodes(root.right)


# 3. Binary Tree Traversals (In-order, Pre-order, Post-order)
def inorder(root):
    if root:
        inorder(root.left)       # 1. Traverse Left
        print(root.value, end=" ") # 2. Visit Root
        inorder(root.right)      # 3. Traverse Right

def preorder(root):
    if root:
        print(root.value, end=" ") # 1. Visit Root
        preorder(root.left)      # 2. Traverse Left
        preorder(root.right)     # 3. Traverse Right

def postorder(root):
    if root:
        postorder(root.left)     # 1. Traverse Left
        postorder(root.right)    # 2. Traverse Right
        print(root.value, end=" ") # 3. Visit Root
```

---

# 7. Recurrence Relations Expansion Proof Protocol

On exams, Prof. Xiao frequently asks students to solve recurrence relations via the **Expansion Method** (Iterative Substitution). To earn full credit, write the expansion in exactly 6 formal steps:

### Recurrence Problem Template:
$$\text{Solve: } T(n) = 2T\left(\frac{n}{2}\right) + n, \quad \text{with base case } T(1) = 1$$

```
================================================================================
STEP-BY-STEP EXAM PROOF FORMAT (Write this verbatim on paper):
================================================================================

Step 1: Write the initial recurrence equation:
        T(n) = 2*T(n/2) + n                                          [Eq. 1]

Step 2: First expansion (substitute T(n/2) = 2*T(n/4) + n/2):
        T(n) = 2 * [ 2*T(n/4) + n/2 ] + n
             = 4*T(n/4) + n + n
             = 4*T(n/4) + 2n                                         [Eq. 2]

Step 3: Second expansion (substitute T(n/4) = 2*T(n/8) + n/4):
        T(n) = 4 * [ 2*T(n/8) + n/4 ] + 2n
             = 8*T(n/8) + n + 2n
             = 8*T(n/8) + 3n                                         [Eq. 3]

Step 4: Express the general pattern after k expansions:
        T(n) = (2^k) * T(n / 2^k) + k * n                            [General Form]

Step 5: Apply base case condition:
        We reach the base case when the subproblem size becomes 1:
        n / (2^k) = 1
        ==> 2^k = n
        ==> k = log2(n)

Step 6: Substitute k = log2(n) and 2^k = n back into the general form:
        T(n) = n * T(1) + log2(n) * n
        Since T(1) = 1:
        T(n) = n*(1) + n * log2(n)
        T(n) = n + n * log2(n)

Conclusion:
        As n -> infinity, the n*log2(n) term dominates.
        Therefore, T(n) = O(n log n)  [Tight Bound: Theta(n log n)]
================================================================================
```

### Accompanying Recursion Tree Diagram for Paper:
```
Level 0:                 ( n )                     --> Work = n
                        /     \
Level 1:           ( n/2 )   ( n/2 )               --> Work = 2 * (n/2) = n
                   /   \     /   \
Level 2:        (n/4)(n/4) (n/4)(n/4)              --> Work = 4 * (n/4) = n
                 ...   ...   ...   ...
Level k:        ( 1 ) ( 1 ) ... ( 1 ) ( 1 )        --> Work = 2^k * 1 = n

Tree Height = log2(n) levels
Total Work  = (Work per level) * (Tree Height)
            = n * log2(n)
            = O(n log n)
```

---

# 8. The 10-Minute Pre-Submission Paper Exam Audit Checklist

Before placing your pen down and handing in your exam paper, run through this rigorous 8-point survival audit:

- [ ] **1. Colons Present**: Did every single `def`, `class`, `if`, `else`, `while`, `for` statement end with a colon `:`?
- [ ] **2. `self` Included**: Does every method signature start with `self` (`def method(self, ...):`)? Does every access to list state use `self.` (`self.head`, `self.tail`, `self.size`)?
- [ ] **3. No Dangling Pointers**: Did you anchor `new_node.right` / `new_node.left` BEFORE breaking `self.head` or `curr.right`?
- [ ] **4. Circular List Guard**: Did circular list traversals use `while curr.right != self.head:` instead of `while curr is not None:` (which causes an infinite loop)?
- [ ] **5. Empty List Handled**: Did every method include the check `if self.head is None:`?
- [ ] **6. Size Variable Updated**: Did every insertion do `self.size += 1` and every deletion do `self.size -= 1`?
- [ ] **7. Indentation Unambiguous**: Are nested blocks visibly indented by at least 2-3 character spaces, and do closing lines clearly return to their parent alignment?
- [ ] **8. Return Values Provided**: Does `pop()` return the popped value? Does `get(index)` return the element value rather than the Node object itself? Does search return `-1` or `None` on failure?
